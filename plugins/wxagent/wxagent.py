# encoding:utf-8

import plugins
from app import db_storage
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from plugins import *
from plugins.wxsop.chat_gpt_bot import OpenaiBot


@plugins.register(
    name="WXAgent",
    desire_priority=900,
    hidden=True,
    desc="AI 角色",
    version="0.1",
    author="gooki.com",
)
class WXAgent(Plugin):
    def __init__(self):
        super().__init__()
        try:
            curdir = os.path.dirname(__file__)
            config_path = os.path.join(curdir, "config.json")
            conf = None
            if not os.path.exists(config_path):
                logger.debug(f"[wxagent]不存在配置文件{config_path}")
            else:
                logger.debug(f"[wxagent]加载配置文件{config_path}")
                with open(config_path, "r", encoding="utf-8") as f:
                    conf = json.load(f)
            self.bot = OpenaiBot(conf["open_ai_api_base"], conf["open_ai_api_key"])
            self.handlers[Event.ON_HANDLE_CONTEXT] = self.on_handle_context
            self.continue_on_miss = conf["continue_on_miss"]
            logger.info("[wxagent] inited.")
        except Exception as e:
            logger.warn("[wxagent] init failed.")
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

        agent_info = db_storage.get_agent_info(bot_wxid)
        logger.debug("[wxagent] content: %s" % content)
        logger.debug("[wxagent] receiver: %s" % receiver)
        logger.debug("[wxagent] bot_wxid: %s" % bot_wxid)
        # 调用 chatgpt 接口
        if agent_info:
            prompt = f"""# 角色信息
{agent_info['role']}

# 背景信息：
{agent_info['background']}

# 对话示例：
{agent_info['examples']}"""
            bot_reply = self.bot.reply(prompt, e_context.econtext['context'])
            logger.debug("[wxagent] reply: %s" % bot_reply)

            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = bot_reply.content

            reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
            e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)

            e_context.action = EventAction.BREAK_PASS


    def get_help_text(self, **kwargs):
        help_text = "AI 角色 回复"
        return help_text

