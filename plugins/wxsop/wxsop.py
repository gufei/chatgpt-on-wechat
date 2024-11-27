# encoding:utf-8
import random
import re
import time
import urllib.parse
import requests

import plugins
from app import db_storage
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from plugins import *
from plugins.wxsop.chat_gpt_bot import OpenaiBot


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
        if not wxinfo:
            return
        server = db_storage.get_server_by_id(wxinfo['server_id'])
        message_record, sop_nodes, source_type, source_id = db_storage.get_next_answers(bot_wxid, contact_wxid, contact_type)
        logger.debug("[wxsop] on_handle_context. message_record: %s" % message_record)
        logger.debug("[wxsop] on_handle_context. sop_nodes: %s" % sop_nodes)
        e_context.econtext['context']['organization_id']= wxinfo['organization_id']

        backup_node_id = -1
        need_judge = False
        # 调用 chatgpt 接口
        if message_record and sop_nodes:
            organization_id = message_record["organization_id"]
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
                reply = self.bot.reply_silent(e_context.econtext['context'], prompt, app=app, app_id=source_id)
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
                                messages.append({
                                    "type": 2,
                                    "message": {
                                        "wxid": receiver,
                                        "filepath": message['content'],
                                        "diyfilename": urllib.parse.unquote(message['meta']['filename'])
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
                    if action_forward['wxid'] != "":
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
                                        forwards.append({
                                            "type": 2,
                                            "message": {
                                                "wxid": forward_wxid,
                                                "filepath": message['content'],
                                                "diyfilename": urllib.parse.unquote(message['meta']['filename'])
                                            }
                                        })
                                # _ = wx_hook_request("/SendFileMsg", data, server['private_ip'], wxinfo['port'])
                if haveVar:
                    contactinfo = db_storage.get_contact_by_wxid(receiver)
                else:
                    contactinfo = {}
                for index, message in enumerate(messages):
                    logger.debug("[wxsop] ------------message-----------: %s" % message)
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
                action_label_del = json.loads(sop_nodes[node_order]['action_label_del'])
                if action_label_add or action_label_del:
                    stages = db_storage.get_stage(organization_id)
                    self.add_tag(e_context,bot_wxid, message_record["contact_id"], contact_type, contact_wxid, action_label_add, action_label_del,
                                 stages, e_context.econtext, organization_id, wxinfo, server)

                e_context.action = EventAction.BREAK_PASS
            else:
                if not self.continue_on_miss:
                    e_context.action = EventAction.BREAK_PASS
        else:
            if not self.continue_on_miss:
                e_context.action = EventAction.BREAK_PASS

    # 为联系人添加标签
    def add_tag(self, e_context: EventContext, bot_wxid, contact_id, contact_type, contact_wxid, action_label_add, action_label_del, stages, context,
                organization_id, wxinfo, server):
        contact_label_ids = db_storage.add_contact_label(contact_id, action_label_add, action_label_del, organization_id)
        match_stages = []
        logger.debug("[wxsop] contact_label_ids: %s" % contact_label_ids)
        logger.debug("[wxsop] stages: %s" % stages)
        for stage in stages:
            if stage["condition_type"] == 1:
                logger.debug("[wxsop] stage: %s" % stage)
                if check_filter(stage, contact_label_ids):
                    match_stages.append(stage)
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
                            messages.append({
                                "type": 2,
                                "message": {
                                    "wxid": contact_wxid,
                                    "filepath": message['content'],
                                    "diyfilename": urllib.parse.unquote(message['meta']['filename'])
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
                if action_forward['wxid'] != "":
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
                                    forwards.append({
                                        "type": 2,
                                        "message": {
                                            "wxid": forward_wxid,
                                            "filepath": message['content'],
                                            "diyfilename": urllib.parse.unquote(message['meta']['filename'])
                                        }
                                    })
            if haveVar:
                contactinfo = db_storage.get_contact_by_wxid(contact_wxid)
            else:
                contactinfo = {}
            for index, message in enumerate(messages):
                # 随机睡眠
                time.sleep(random.uniform(2.0, 5.0))
                if message["type"] == 1:
                    if haveVar:
                        message["message"]["msg"] = var_replace(message["message"]["msg"],
                                                                contactinfo)
                    _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])

                    _ = db_storage.create_message_record(3, bot_wxid, contact_id,
                                                         contact_type,
                                                         contact_wxid, message["type"],
                                                         message['message']['msg'], {}, 3,
                                                         stage["id"], index,
                                                         organization_id)
                else:
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
                    _ = wx_hook_request(e_context,"/SendTextMsg", message["message"], server.get('private_ip') if server else None,
                                        wxinfo['port'])
                else:
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
                self.add_tag(e_context,bot_wxid, contact_id, contact_type, contact_wxid, add_labels, rem_labels, stages, context,
                             organization_id, wxinfo, server)

    def get_help_text(self, **kwargs):
        help_text = "SOP 过滤"
        return help_text


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
            e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


def contains_placeholder(s: str) -> bool:
    pattern = r'\$\{.*?\}'
    return bool(re.search(pattern, s))


def var_replace(s: str, contactinfo: dict) -> str:
    s = s.replace("${nickname}", contactinfo["nickname"])
    return s


def split_string(input_string):
    # 定义正则表达式，匹配中文逗号、英文逗号和顿号
    pattern = r'[，,、]'
    # 使用re.split方法分割字符串
    result = re.split(pattern, input_string)
    return result
