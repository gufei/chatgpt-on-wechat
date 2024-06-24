# encoding:utf-8

import requests
import plugins
from bot.bot_factory import create_bot
from bridge.bridge import Bridge
from bridge.context import ContextType, Context
from bridge.reply import Reply, ReplyType
from channel.wechat.wxhook_channel import wx_hook_request
from plugins import *
from plugins.wxsop.db.DBStorage import DBStorage


@plugins.register(
    name="WXSop",
    desire_priority=901,
    hidden=True,
    desc="SOP 匹配过滤",
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
            # 创建数据库对象
            self.db = DBStorage(conf["host"], conf["port"], conf["user"], conf["password"], conf["database"])
            self.bot = create_bot("chatGPT")
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
            logger.info("[wxsop] inited.")
        except Exception as e:
            logger.warn("[wxsop] init failed.")
            raise e

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return

        bot_wxid = e_context.econtext['channel'].user_id
        contact_wxid = e_context.econtext['context'].kwargs['session_id']
        receiver = e_context.econtext['context'].kwargs['receiver']
        # nickname = e_context.econtext['context'].kwargs['msg'].from_user_nickname
        content = e_context["context"].content.strip()
        if receiver == contact_wxid:
            contact_type = 1
        else:
            contact_type = 2

        message_record, sop_nodes = self.db.get_next_answers(bot_wxid, contact_wxid, contact_type)
        logger.debug("[wxsop] on_handle_context. message_record: %s" % message_record)
        logger.debug("[wxsop] on_handle_context. sop_nodes: %s" % sop_nodes)

        # 调用 chatgpt 接口
        if message_record and sop_nodes:
            prompt = f"""# 任务
你好，请根据用户发送的内容，判断命中了哪个 SOP 节点。

# 用户发送内容：{content}

# 节点列表
            """
            for index, sop_node in enumerate(sop_nodes):
                if sop_node['condition_list']:
                    prompt += f"""node_order: {index}
命中条件：{sop_node['condition_list']}
"""
                else:
                    prompt += f"""node_order: {index}
命中条件：用户发送任意内容
"""
            prompt += f"""# 判断方式：
用户发送的内容与节点命中条件语义相同既算命中

# 回复要求
- 如果有命中的节点：则仅回复 node_order 的值（如命中多个节点，则仅回复最小值），例如回复 0
- 如果没命中的节点：则仅回复一个单词 None"""
            reply = self.bot.reply(prompt, e_context.econtext['context'])
            logger.debug("[wxsop] reply: %s" % reply)
            if reply.content != "None":
                # 将 reply.content 从 str 转换为 int
                node_order = int(reply.content)
                # sop_nodes[node_order]['action_message']的值为 json str ，将其转换为字典
                action_messages = json.loads(sop_nodes[node_order]['action_message'])

                for message in action_messages:
                    type = int(message['type'])

                    reply = Reply()
                    reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                    reply.content = message['content']
                    reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
                    e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)

                    status = 3 if e_context.econtext.get('context', {}).get('is_success') else 4

                    _ = self.db.create_message_record(status, bot_wxid, message_record["contact_id"], contact_type,
                                                      contact_wxid, type, message['content'], 3,
                                                      message_record["source_id"], sop_nodes[node_order]["id"])

                action_label = json.loads(sop_nodes[node_order]['action_label'])
                if action_label:
                    stages = self.db.get_stage()
                    self.add_tag(bot_wxid, message_record["contact_id"], contact_type, contact_wxid, action_label, stages, e_context.econtext)

                e_context.action = EventAction.BREAK_PASS

    # 为联系人添加标签
    def add_tag(self, bot_wxid, contact_id, contact_type, contact_wxid, label_ids, stages, context):
        contact_label_ids = self.db.add_contact_label(contact_id, label_ids)
        match_stages = []
        logger.debug("[wxsop] contact_label_ids: %s" % contact_label_ids)
        logger.debug("[wxsop] stages: %s" % stages)
        for stage in stages:
            if stage["condition_type"] == 1:
                logger.debug("[wxsop] stage: %s" % stage)
                if check_filter(stage, contact_label_ids):
                    logger.debug("[wxsop] check_filter")
                    match_stages.append(stage)
        for stage in match_stages:
            is_message_send = self.db.check_message_record(contact_wxid, 3, stage["id"], 0)
            if is_message_send:
                continue
            if stage["action_message"]:
                action_message = json.loads(stage['action_message'])
                for message in action_message:
                    type = int(message['type'])

                    lastrowid = self.db.create_message_record(2, bot_wxid, contact_id, contact_type, contact_wxid,
                                                      type, message['content'], 3, stage["id"], 0)
                    if lastrowid:
                        reply = Reply()
                        reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                        reply.content = message['content']
                        reply = context['channel']._decorate_reply(context['context'], reply)
                        context['channel']._send_reply(context.get('context', {}), reply)

                        if context.get('context', {}).get('is_success'):
                            self.db.update_message_record(lastrowid, 3)
                        else:
                            self.db.update_message_record(lastrowid, 4, "SOP send failed")

            if stage["action_label"]:
                action_label = json.loads(stage['action_label'])
                self.add_tag(bot_wxid, contact_id, contact_type, contact_wxid, action_label, stages, context)

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
