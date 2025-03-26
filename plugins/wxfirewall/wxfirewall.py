# encoding:utf-8

import plugins
from app import db_storage
from bot.chatgpt.chat_gpt_bot import parse_markdown
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from plugins import *
from plugins.wxsop.chat_gpt_bot import OpenaiBot
import requests


@plugins.register(
    name="WXFirewall",
    desire_priority=902,
    hidden=True,
    desc="防火墙，防止机器人互聊",
    version="0.1",
    author="gooki.com",
)
class WXFirewall(Plugin):
    def __init__(self):
        super().__init__()
        try:
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
            logger.info("[wxfirewall] inited.")
        except Exception as e:
            logger.warn("[wxfirewall] init failed.")
            raise e

    def on_handle_context(self, e_context: EventContext):
        # bot_wxid = e_context.econtext['context'].kwargs['wxid']
        contact_wxid = e_context.econtext['context'].kwargs['session_id']
        # receiver = e_context.econtext['context'].kwargs['receiver']

        agent_info = db_storage.get_info_by_wxid(contact_wxid)

        if agent_info:
            logger.info("[WXFirewall] 对方为机器问不回复")
            e_context.action = EventAction.BREAK_PASS
