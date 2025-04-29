# encoding:utf-8
import random
import re
import time
import urllib.parse
import requests

import plugins
from app import db_storage
from bridge.reply import Reply, ReplyType
from plugins import *
from plugins.wxsop.chat_gpt_bot import OpenaiBot
from urllib.parse import urlparse
from pathlib import Path

@plugins.register(
    name="WXSop",
    desire_priority=901,
    hidden=True,
    desc="SOP",
    version="0.1",
    author="gooki.com",
)
class WXSop(Plugin):
    def __init__(self):
        super().__init__()
        try:
            curdir = os.path.dirname(__file__)
            config_path = os.path.join(curdir, "config.json")
            conf = None
            if not os.path.exists(config_path):
                logger.debug(f"[wxsop]不存在配置文件{config_path}")
            else:
                logger.debug(f"[wxsop]加载配置文件{config_path}")
                with open(config_path, "r", encoding="utf-8") as f:
                    conf = json.load(f)
            self.bot = OpenaiBot(conf["open_ai_api_base"], conf["open_ai_api_key"], conf["model"])
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
            self.continue_on_miss = conf["continue_on_miss"]
            logger.info("[wxsop] inited.")
        except Exception as e:
            logger.warn("[wxsop] init failed.")
            raise e

    def on_handle_context(self, e_context: EventContext):

        bot_wxid = e_context.econtext['context'].kwargs['wxid']
        contact_wxid = e_context.econtext['context'].kwargs['session_id']
        receiver = e_context.econtext['context'].kwargs['receiver']
        # nickname = e_context.econtext['context'].kwargs['msg'].from_user_nickname
        content = e_context["context"].content.strip()
        if receiver == contact_wxid:
            contact_type = 1
        else:
            contact_type = 2

        wxinfo = db_storage.get_info_by_wxid(bot_wxid)
        logger.debug("[wxsop] wxinfo: %s" % wxinfo)
        if not wxinfo:
            return

        tagging_label_add = []
        organization_id = wxinfo.get("organization_id")
        logger.debug("[wxsop] organization_id: %s" % organization_id)
        if organization_id:
            conditions_group = db_storage.get_label_tagging_by_orgid(organization_id)
            logger.debug("[wxsop] conditions_group: %s" % conditions_group)
            if conditions_group:
                tagging_label_add = match_text_with_conditions(content, conditions_group)
        logger.debug("[wxsop] tagging_label_add: %s" % tagging_label_add)
        server = db_storage.get_server_by_id(wxinfo['server_id'])
        message_record, sop_nodes, source_type, source_id = db_storage.get_next_answers(bot_wxid, contact_wxid, contact_type)
        organization_id = wxinfo.get("organization_id")
        logger.debug("[wxsop] on_handle_context. message_record: %s" % message_record)
        logger.debug("[wxsop] on_handle_context. sop_nodes: %s" % sop_nodes)
        e_context.econtext['context']['organization_id']= wxinfo['organization_id']

        backup_node_id = -1
        need_judge = False
        # 调用 chatgpt 接口
        if message_record and sop_nodes:
            if contains_placeholder(message_record["content"]):
                contactinfo = db_storage.get_contact_by_wxid(receiver, bot_wxid)
                message_record["content"] = var_replace(message_record["content"], contactinfo)
            # organization_id = message_record["organization_id"]
            prompt = f"""# 任务
请根据历史消息，判断用户回复的内容或深层意图，与哪个节点的意图相匹配。

# 历史消息：
助手发送：{message_record["content"]}
用户回复：{content}

# 节点列表："""
            for index, sop_node in enumerate(sop_nodes):
                # condition_list = json.loads(sop_node['condition_list'])
                if sop_node['condition_list'] != '[""]':
                    need_judge = True
                    prompt += f"""
节点 id: {index}
节点意图：{sop_node['condition_list']}
"""
                else:
                    if sop_node['no_reply_condition'] == 0:
                        backup_node_id = index
            #                     prompt += f"""
            # 节点 id: {index}
            # 命中条件：用户发送任意内容
            # """
            prompt += f"""
# 回复要求
- 如果命中节点：则仅回复节点 id 数字（如命中多个节点，则仅回复最小值）
- 如果未命中节点：则仅回复一个单词: None"""
            if need_judge:
                if source_type == 3:
                    app = 4
                else:
                    app = 5
                reply = self.bot.reply_silent_contentless(e_context.econtext['context'], prompt, app=app, app_id=source_id)
            else:
                reply = Reply()
                reply.content = "None"
            logger.debug("[wxsop] reply: %s" % reply)
            if reply.content == "None" and backup_node_id != -1:
                reply.content = str(backup_node_id)
            if reply.content != "None":
                # 将 reply.content 从 str 转换为 int
                node_order = int(reply.content)
                # sop_nodes[node_order]['action_message']的值为 json str ，将其转换为字典
                messages = []
                forwards = []
                haveVar = False

                if sop_nodes[node_order]['action_message'] is not None:
                    action_messages = json.loads(sop_nodes[node_order]['action_message'])
                    for index, message in enumerate(action_messages):
                        if message['content'] != "":
                            type = int(message['type'])

                            if type == 1:
                                haveVar = contains_placeholder(message['content'])
                                messages.append({
                                    "type": 1,
                                    "message": {
                                        "wxid": receiver,
                                        "msg": message['content']
                                    }
                                })
                            else:
                                url = message['content']
                                # 解析 URL
                                parsed_url = urlparse(url)
                                # 获取路径部分
                                path = parsed_url.path
                                # 使用 Path 类提取文件名
                                filename = Path(path).name
                                messages.append({
                                    "type": 2,
                                    "message": {
                                        "wxid": receiver,
                                        "filepath": message['content'],
                                        "diyfilename": urllib.parse.unquote(filename)
                                    }
                                })

                if len(messages) == 0:
                    _ = db_storage.create_message_record(3, bot_wxid, message_record["contact_id"],
                                                         contact_type,
                                                         contact_wxid, 1, "", {}, 4,
                                                         sop_nodes[node_order]["id"], 0, organization_id)

                    # logger.debug("[wxsop] reply: %s" % reply)
                    # reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
                    # e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)

                    # status = 3 if e_context.econtext.get('context', {}).get('is_success') else 4
                    #
                    # _ = db_storage.create_message_record(status, bot_wxid, message_record["contact_id"],
                    #                                      contact_type,
                    #                                      contact_wxid, type, message['content'], meta, 4,
                    #                                      sop_nodes[node_order]["id"], index, organization_id)

                if sop_nodes[node_order]['action_forward'] is not None:
                    action_forward = json.loads(sop_nodes[node_order]['action_forward'])
                    if action_forward and action_forward.get('wxid', "") != "":
                        forward_wxids = split_string(action_forward['wxid'])
                        for forward_wxid in forward_wxids:
                            for index, message in enumerate(action_forward['action']):
                                if message['content'] != "":
                                    type = int(message['type'])
                                    if type == 1:
                                        haveVar = contains_placeholder(message['content'])
                                        forwards.append({
                                            "type": 1,
                                            "message": {
                                                "wxid": forward_wxid,
                                                "msg": message['content']
                                            }
                                        })
                                        # _ = wx_hook_request("/SendTextMsg", data, server['private_ip'], wxinfo['port'])
                                    else:
                                        url = message['content']
                                        # 解析 URL
                                        parsed_url = urlparse(url)
                                        # 获取路径部分
                                        path = parsed_url.path
                                        # 使用 Path 类提取文件名
                                        filename = Path(path).name
                                        forwards.append({
                                            "type": 2,
                                            "message": {
                                                "wxid": forward_wxid,
                                                "filepath": message['content'],
                                                "diyfilename": urllib.parse.unquote(filename)
                                            }
                                        })
                                # _ = wx_hook_request("/SendFileMsg", data, server['private_ip'], wxinfo['port'])
                if haveVar:
                    contactinfo = db_storage.get_contact_by_wxid(receiver, bot_wxid)
                else:
                    contactinfo = {}
                for index, message in enumerate(messages):
                    # 随机睡眠
                    time.sleep(random.uniform(2.0, 5.0))

                    if message["type"] == 1:
                        if haveVar:
                            message["message"]["msg"] = var_replace(message["message"]["msg"], contactinfo)
                        _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None, wxinfo.get('port'))

                        _ = db_storage.create_message_record(3, bot_wxid, message_record["contact_id"],
                                                             contact_type,
                                                             contact_wxid, message["type"],
                                                             message['message']['msg'], {}, 4,
                                                             sop_nodes[node_order]["id"], index, organization_id)
                    else:
                        _ = wx_hook_request(e_context, "/SendFileMsg", message["message"], server.get('private_ip') if server else None, wxinfo.get('port'))

                        _ = db_storage.create_message_record(3, bot_wxid, message_record["contact_id"],
                                                             contact_type,
                                                             contact_wxid, message["type"],
                                                             message['message']['filepath'],
                                                             {"filename": message['message']['diyfilename']}, 4,
                                                             sop_nodes[node_order]["id"], index, organization_id)

                for message in forwards:
                    # 随机睡眠
                    time.sleep(random.uniform(2.0, 5.0))
                    if message["type"] == 1:
                        if haveVar:
                            message["message"]["msg"] = var_replace(message["message"]["msg"], contactinfo)
                        _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None,
                                            wxinfo['port'])
                    else:
                        _ = wx_hook_request(e_context, "/SendFileMsg", message["message"], server.get('private_ip') if server else None,
                                            wxinfo['port'])
                        # status = 3 if e_context.econtext.get('context', {}).get('is_success') else 4
                        #
                        # _ = db_storage.create_message_record(status, bot_wxid, message_record["contact_id"],
                        #                                      contact_type,
                        #                                      contact_wxid, type, message['content'], meta, 4,
                        #                                      sop_nodes[node_order]["id"], index, organization_id)

                action_label_add = json.loads(sop_nodes[node_order]['action_label_add'])
                if tagging_label_add:
                    action_label_add = action_label_add + tagging_label_add
                action_label_del = json.loads(sop_nodes[node_order]['action_label_del'])
                if action_label_add or action_label_del:
                    stages = db_storage.get_stage(organization_id)
                    self.add_tag(e_context,bot_wxid, message_record["contact_id"], contact_type, contact_wxid, action_label_add, action_label_del,
                                 stages, e_context.econtext, organization_id, wxinfo, server)

                e_context.action = EventAction.BREAK_PASS
            else:
                e_context.econtext['context']['sop_unmatched'] = message_record["content"]
                if tagging_label_add:
                    stages = db_storage.get_stage(organization_id)
                    contact_id = 0
                    if not message_record:
                        contact_info = db_storage.get_contact_by_wxid(contact_wxid, bot_wxid)
                        if contact_info:
                            contact_id = contact_info.get("id")
                    else:
                        contact_id = message_record.get("contact_id", 0)
                    if contact_id:
                        is_send_message = self.add_tag(e_context, bot_wxid, contact_id, contact_type, contact_wxid,
                                     tagging_label_add, [],
                                     stages, e_context.econtext, organization_id, wxinfo, server)
                        if is_send_message:
                            e_context.action = EventAction.BREAK_PASS
                        else:
                            if not self.continue_on_miss:
                                e_context.action = EventAction.BREAK_PASS
                else:
                    if not self.continue_on_miss:
                        e_context.action = EventAction.BREAK_PASS
        else:
            if tagging_label_add:
                logger.debug("[wxsop] tagging_label_add2: %s" % tagging_label_add)
                stages = db_storage.get_stage(organization_id)
                contact_id = 0
                if not message_record:
                    contact_info = db_storage.get_contact_by_wxid(contact_wxid, bot_wxid)
                    if contact_info:
                        contact_id = contact_info.get("id")
                else:
                    contact_id = message_record.get("contact_id", 0)
                logger.debug("[wxsop] contact_id: %s" % contact_id)
                if contact_id:
                    is_send_message = self.add_tag(e_context, bot_wxid, contact_id, contact_type, contact_wxid,
                                 tagging_label_add, [],
                                 stages, e_context.econtext, organization_id, wxinfo, server)
                    if is_send_message:
                        e_context.action = EventAction.BREAK_PASS
                    else:
                        if not self.continue_on_miss:
                            e_context.action = EventAction.BREAK_PASS
            else:
                if not self.continue_on_miss:
                    e_context.action = EventAction.BREAK_PASS

    # 为联系人添加标签
    def add_tag(self, e_context: EventContext, bot_wxid, contact_id, contact_type, contact_wxid, action_label_add, action_label_del, stages, context,
                organization_id, wxinfo, server, is_send_message=False):
        # is_send_message = False
        contact_label_ids = db_storage.add_contact_label(contact_id, action_label_add, action_label_del, organization_id)
        match_stages = []
        unmatch_stages = []
        logger.debug("[wxsop] contact_label_ids: %s" % contact_label_ids)
        logger.debug("[wxsop] stages: %s" % stages)
        for stage in stages:
            if stage["condition_type"] == 1 and contact_label_ids:
                logger.debug("[wxsop] stage: %s" % stage)
                if check_filter(stage, contact_label_ids):
                    match_stages.append(stage)
                else:
                    unmatch_stages.append(stage)
        for stage in match_stages:
            is_message_send = db_storage.check_message_record(contact_wxid, 3, stage["id"], 0)
            if is_message_send:
                continue
            messages = []
            forwards = []
            haveVar = False
            if stage["action_message"]:
                action_message = json.loads(stage['action_message'])
                for index, message in enumerate(action_message):
                    if message['content'] != "":
                        type = int(message['type'])

                        if type == 1:
                            haveVar = contains_placeholder(message['content'])
                            messages.append({
                                "type": 1,
                                "message": {
                                    "wxid": contact_wxid,
                                    "msg": message['content']
                                }
                            })
                        else:
                            url = message['content']
                            # 解析 URL
                            parsed_url = urlparse(url)
                            # 获取路径部分
                            path = parsed_url.path
                            # 使用 Path 类提取文件名
                            filename = Path(path).name

                            messages.append({
                                "type": 2,
                                "message": {
                                    "wxid": contact_wxid,
                                    "filepath": message['content'],
                                    "diyfilename": urllib.parse.unquote(filename)
                                }
                            })
                        # lastrowid = db_storage.create_message_record(2, bot_wxid, contact_id, contact_type, contact_wxid,
                        #                                              type, message['content'], meta, 3, stage["id"], index,
                        #                                              organization_id)
            if len(messages) == 0:
                _ = db_storage.create_message_record(3, bot_wxid, contact_id,
                                                     contact_type,
                                                     contact_wxid, 1, "", {}, 3,
                                                     stage["id"], 0, organization_id)
                        # if lastrowid:
                        #     reply = Reply()
                        #     reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                        #     reply.content = message['content']
                        #     reply = context['channel']._decorate_reply(context['context'], reply)
                        #     if type == 2:
                        #         context.get('context', {})["diyfilename"] = message['meta']['filename']
                        #     logger.debug("[wxsop] context: %s" % context.get('context', {}))
                        #     context['channel']._send_reply(context.get('context', {}), reply)
                        #
                        #     if context.get('context', {}).get('is_success'):
                        #         db_storage.update_message_record(lastrowid, 3)
                        #     else:
                        #         db_storage.update_message_record(lastrowid, 4, "SOP send failed")

            if stage["action_forward"]:
                action_forward = json.loads(stage['action_forward'])
                if action_forward and action_forward.get('wxid', "") != "":
                    forward_wxids = split_string(action_forward['wxid'])
                    for forward_wxid in forward_wxids:
                        for index, message in enumerate(action_forward['action']):
                            if message['content'] != "":
                                type = int(message['type'])

                                if type == 1:
                                    haveVar = contains_placeholder(message['content'])
                                    forwards.append({
                                        "type": 1,
                                        "message": {
                                            "wxid": forward_wxid,
                                            "msg": message['content']
                                        }
                                    })
                                    # _ = wx_hook_request("/SendTextMsg", data, server['private_ip'], wxinfo['port'])
                                else:
                                    url = message['content']
                                    # 解析 URL
                                    parsed_url = urlparse(url)
                                    # 获取路径部分
                                    path = parsed_url.path
                                    # 使用 Path 类提取文件名
                                    filename = Path(path).name

                                    forwards.append({
                                        "type": 2,
                                        "message": {
                                            "wxid": forward_wxid,
                                            "filepath": message['content'],
                                            "diyfilename": urllib.parse.unquote(filename)
                                        }
                                    })
            if haveVar:
                contactinfo = db_storage.get_contact_by_wxid(contact_wxid, bot_wxid)
            else:
                contactinfo = {}
            for index, message in enumerate(messages):
                # 随机睡眠
                time.sleep(random.uniform(2.0, 5.0))
                if message["type"] == 1:
                    if haveVar:
                        message["message"]["msg"] = var_replace(message["message"]["msg"],
                                                                contactinfo)
                    is_send_message = True
                    _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])

                    _ = db_storage.create_message_record(3, bot_wxid, contact_id,
                                                         contact_type,
                                                         contact_wxid, message["type"],
                                                         message['message']['msg'], {}, 3,
                                                         stage["id"], index,
                                                         organization_id)
                else:
                    is_send_message = True
                    _ = wx_hook_request(e_context,"/SendFileMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])

                    _ = db_storage.create_message_record(3, bot_wxid, contact_id,
                                                         contact_type,
                                                         contact_wxid, message["type"],
                                                         message['message']['filepath'],
                                                         {"filename": message['message'][
                                                             'diyfilename']}, 3,
                                                         stage["id"], index,
                                                         organization_id)

            for message in forwards:
                # 随机睡眠
                time.sleep(random.uniform(2.0, 5.0))
                if message["type"] == 1:
                    if haveVar:
                        message["message"]["msg"] = var_replace(message["message"]["msg"], contactinfo)
                    is_send_message = True
                    _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])
                else:
                    is_send_message = True
                    _ = wx_hook_request(e_context,"/SendFileMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])
                                # lastrowid = db_storage.create_message_record(2, bot_wxid, contact_id, contact_type, contact_wxid,
                                #                                              type, message['content'], meta, 3, stage["id"], index,
                                #                                              organization_id)
                                # if lastrowid:
                                #     reply = Reply()
                                #     reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                                #     reply.content = message['content']
                                #     reply = context['channel']._decorate_reply(context['context'], reply)
                                #     if type == 2:
                                #         context.get('context', {})["diyfilename"] = message['meta']['filename']
                                #     logger.debug("[wxsop] context: %s" % context.get('context', {}))
                                #     context['channel']._send_reply(context.get('context', {}), reply)
                                #
                                #     if context.get('context', {}).get('is_success'):
                                #         db_storage.update_message_record(lastrowid, 3)
                                #     else:
                                #         db_storage.update_message_record(lastrowid, 4, "SOP send failed")

            if stage["action_label_add"] or stage["action_label_del"]:
                add_labels = json.loads(stage['action_label_add'])
                rem_labels = json.loads(stage['action_label_del'])
                is_send_message = self.add_tag(e_context,bot_wxid, contact_id, contact_type, contact_wxid, add_labels, rem_labels, unmatch_stages, context,
                             organization_id, wxinfo, server, is_send_message)
        return is_send_message

    def get_help_text(self, **kwargs):
        help_text = "SOP 过滤"
        return help_text


def match_text_with_conditions(text, conditions_group):
    # 初始化一个列表用于存储所有命中的 action_label_add
    matched_labels = []

    # 遍历每个条件组
    logger.debug("[wxsop] match_text_with_conditions group: %s" % text)
    for group in conditions_group:
        logger.debug("[wxsop] match_text_with_conditions group: %s" % group)
        conditions = group.get("conditions", "")
        action_label_add_str = group.get("action_label_add", [])
        regex = re.compile(conditions)
        # 检查当前条件组中的任意一个条件是否在文本中出现
        logger.debug("[wxsop] match_text_with_conditions action_label_add: %s" % action_label_add_str)
        logger.debug("[wxsop] match_text_with_conditions conditions: %s" % conditions)
        logger.debug("[wxsop] match_text_with_conditions regex.search(text): %s" % regex.search(text))
        logger.debug("[wxsop] match_text_with_conditions bool(regex.search(text): %s" % bool(regex.search(text)))
        if bool(regex.search(text)):
            # 如果命中，则将对应的 action_label_add 加入结果列表
            action_label_add = json.loads(action_label_add_str)
            matched_labels.extend(action_label_add)

    return matched_labels

def check_filter(filter, contact_label_ids):
    condition_operator = filter['condition_operator']
    condition_list = json.loads(filter['condition_list'])

    if condition_operator == 1:
        # All conditions must be met
        for condition in condition_list:
            if condition['equal'] == 1 and not set(condition['labelIdList']).issubset(set(contact_label_ids)):
                return False
            elif condition['equal'] == 2 and set(condition['labelIdList']).issubset(set(contact_label_ids)):
                return False
        return True
    elif condition_operator == 2:
        # Any condition can be met
        for condition in condition_list:
            if condition['equal'] == 1 and set(condition['labelIdList']).issubset(set(contact_label_ids)):
                return True
            elif condition['equal'] == 2 and not set(condition['labelIdList']).issubset(set(contact_label_ids)):
                return True
        return False


def wx_hook_request(e_context: EventContext, path, data, private_ip, port):
    try:
        if private_ip:
            # path判断是不是/开头
            if not path.startswith("/"):
                path = "/" + path
            url = f"http://{private_ip}:{port}{path}"
            headers = {
                "Content-Type": "application/json",
            }
            res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
            logger.debug(f"[wx_hook] send message success, url: {url} data: {data} res: {res.json(strict=False)}")
            return res.json(strict=False)
        else:
            reply = Reply()
            content = data.get("msg")
            if content:
                reply.type = ReplyType.TEXT
                reply.content = content
            else:
                reply.type = ReplyType.FILE
                reply.content = data.get("filepath")

            reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
            reply.receiver = data.get("wxid")
            e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


def contains_placeholder(s: str) -> bool:
    pattern = r'\$\{.*?\}'
    return bool(re.search(pattern, s))


def var_replace(s: str, contactinfo: dict) -> str:
    s = s.replace("${nickname}", contactinfo.get("nickname", ""))
    s = s.replace("${cname}", contactinfo.get("cname", ""))
    s = s.replace("${ctitle}", contactinfo.get("ctitle", ""))
    s = s.replace("${cidcard_no}", contactinfo.get("cidcard_no", ""))
    s = s.replace("${carea}", contactinfo.get("carea", ""))
    s = s.replace("${cbirtharea}", contactinfo.get("cbirtharea", ""))
    s = s.replace("${cbirthday}", contactinfo.get("cbirthday", ""))

    sex_index = contactinfo.get("sex", 0)
    sex = ""
    if sex_index == 1:
        sex = "男"
    elif sex_index == 2:
        sex = "女"
    s = s.replace("${sex}", sex)

    age_index = contactinfo.get("cage", 0)
    age = ""
    if age_index:
        age = str(age_index)
    s = s.replace("${cage}", age)
    return s


def split_string(input_string):
    # 定义正则表达式，匹配中文逗号、英文逗号和顿号
    pattern = r'[，,、]'
    # 使用re.split方法分割字符串
    result = re.split(pattern, input_string)
    return result
