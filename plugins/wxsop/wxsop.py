# encoding:utf-8

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
            self.bot = OpenaiBot(conf["open_ai_api_base"], conf["open_ai_api_key"])
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
            self.continue_on_miss = conf["continue_on_miss"]
            logger.info("[wxsop] inited.")
        except Exception as e:
            logger.warn("[wxsop] init failed.")
            raise e

    def on_handle_context(self, e_context: EventContext):
        if e_context["context"].type != ContextType.TEXT:
            return
        
        bot_wxid = e_context.econtext['context'].kwargs['wxid']
        contact_wxid = e_context.econtext['context'].kwargs['session_id']
        receiver = e_context.econtext['context'].kwargs['receiver']
        # nickname = e_context.econtext['context'].kwargs['msg'].from_user_nickname
        content = e_context["context"].content.strip()
        if receiver == contact_wxid:
            contact_type = 1
        else:
            contact_type = 2

        message_record, sop_nodes = db_storage.get_next_answers(bot_wxid, contact_wxid, contact_type)
        logger.debug("[wxsop] on_handle_context. message_record: %s" % message_record)
        logger.debug("[wxsop] on_handle_context. sop_nodes: %s" % sop_nodes)

        backup_node_id = -1
        # 调用 chatgpt 接口
        if message_record and sop_nodes:
            organization_id = message_record["organization_id"]
            prompt = f"""# 任务
请根据 用户发送内容，判断命中了 节点列表 中的哪个 节点。

# 用户发送内容：{content}

# 节点列表："""
            for index, sop_node in enumerate(sop_nodes):
                # condition_list = json.loads(sop_node['condition_list'])
                if sop_node['condition_list'] != '[""]':
                    prompt += f"""
节点 id: {index}
命中条件：{sop_node['condition_list']}
"""
                else:
                    backup_node_id = index
#                     prompt += f"""
# 节点 id: {index}
# 命中条件：用户发送任意内容
# """
            prompt += f"""
# 判断方式：
「用户发送内容」与「节点命中条件」的意图相同即算命中节点，如都为肯定或否定等。而意图不同则不算命中

# 回复要求
- 如果命中节点：则仅回复节点 id 数字（如命中多个节点，则仅回复最小值）
- 如果未命中节点：则仅回复一个单词: None"""

            reply = self.bot.reply(prompt, e_context.econtext['context'])
            logger.debug("[wxsop] reply: %s" % reply)
            if reply.content == "None" and backup_node_id != -1:
                reply.content = str(backup_node_id)
            if reply.content != "None":
                # 将 reply.content 从 str 转换为 int
                node_order = int(reply.content)
                # sop_nodes[node_order]['action_message']的值为 json str ，将其转换为字典
                action_messages = json.loads(sop_nodes[node_order]['action_message'])

                for index, message in enumerate(action_messages):
                    type = int(message['type'])

                    reply = Reply()
                    reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                    reply.content = message['content']
                    if type == 2:
                        e_context.econtext.get('context', {})["diyfilename"] = message['meta']['filename']
                        meta = {
                            "filename": message['meta']['filename']
                        }
                    else:
                        meta = {}
                    logger.debug("[wxsop] reply: %s" % reply)
                    reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
                    e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)

                    status = 3 if e_context.econtext.get('context', {}).get('is_success') else 4

                    _ = db_storage.create_message_record(status, bot_wxid, message_record["contact_id"], contact_type,
                                                      contact_wxid, type, message['content'], meta,4,
                                                      sop_nodes[node_order]["id"], index, organization_id)

                action_label = json.loads(sop_nodes[node_order]['action_label'])
                if action_label:
                    stages = db_storage.get_stage(organization_id)
                    self.add_tag(bot_wxid, message_record["contact_id"], contact_type, contact_wxid, action_label, stages, e_context.econtext, organization_id)

                e_context.action = EventAction.BREAK_PASS
            else:
                if not self.continue_on_miss:
                    e_context.action = EventAction.BREAK_PASS
        else:
            if not self.continue_on_miss:
                e_context.action = EventAction.BREAK_PASS

    # 为联系人添加标签
    def add_tag(self, bot_wxid, contact_id, contact_type, contact_wxid, label_ids, stages, context, organization_id: int):
        logger.debug("[wxsop] label_ids: %s" % label_ids)
        contact_label_ids = db_storage.add_contact_label(contact_id, label_ids, organization_id)
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
            is_message_send = db_storage.check_message_record(contact_wxid, 3, stage["id"], 0)
            if is_message_send:
                continue
            if stage["action_message"]:
                action_message = json.loads(stage['action_message'])
                for index, message in enumerate(action_message):
                    type = int(message['type'])

                    if type == 2:
                        meta = {
                            "filename": message['meta']['filename']
                        }
                    else:
                        meta = {}

                    lastrowid = db_storage.create_message_record(2, bot_wxid, contact_id, contact_type, contact_wxid,
                                                      type, message['content'], meta, 3, stage["id"], index, organization_id)
                    if lastrowid:
                        reply = Reply()
                        reply.type = ReplyType.TEXT if type == 1 else ReplyType.FILE
                        reply.content = message['content']
                        reply = context['channel']._decorate_reply(context['context'], reply)
                        if type == 2:
                            context.get('context', {})["diyfilename"] = message['meta']['filename']
                        logger.debug("[wxsop] context: %s" % context.get('context', {}))
                        context['channel']._send_reply(context.get('context', {}), reply)

                        if context.get('context', {}).get('is_success'):
                            db_storage.update_message_record(lastrowid, 3)
                        else:
                            db_storage.update_message_record(lastrowid, 4, "SOP send failed")

            if stage["action_label"]:
                action_label = json.loads(stage['action_label'])
                self.add_tag(bot_wxid, contact_id, contact_type, contact_wxid, action_label, stages, context, organization_id)

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
