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
        bot_wxid = e_context.econtext['context'].kwargs['wxid']
        logger.info("[WXAgent] bot_wxid={}".format(bot_wxid))
        contact_wxid = e_context.econtext['context'].kwargs['session_id']
        receiver = e_context.econtext['context'].kwargs['receiver']
        # nickname = e_context.econtext['context'].kwargs['msg'].from_user_nickname
        content = e_context["context"].content.strip()
        if receiver == contact_wxid:
            contact_type = 1
        else:
            contact_type = 2

        agent_info = db_storage.get_agent_info(bot_wxid)
        logger.info("[WXAgent] agent_info={}".format(agent_info))
        # 调用 chatgpt 接口
        if agent_info:
            # 优化问题
            expand_system_prompt = f"""# 任务：
请根据上下文信息，优化用户发送的最后一条消息，补齐消息中可能缺失的主语、谓语、宾语、定语、状语、补语句子成分。

# 用户发送的最后一条消息：{content}

# 回复要求
1. 直接输出优化后的消息"""
            expand_bot_reply = self.bot.reply_silent(e_context.econtext['context'], expand_system_prompt)
            logger.debug("[wxagent] expand_bot_reply: %s" % expand_bot_reply.content)

            answer = chat_service_openai_like(agent_info['dataset_id'], expand_bot_reply.content)

            system_prompt = f"""# 角色
{agent_info['role']}

# 背景：
{agent_info['background']}
"""
            if answer is not None:
                system_prompt += """# 相关知识：
"""
                for data in answer:
                    system_prompt += f"""问题：{data['q']}
答案：{data['a']}
"""
            system_prompt += """# 回复要求：
1. 直接以角色设定的角度回答问题，并以第一人称输出。
2. 不要在回复前加角色、姓名。
3. 回复要正式"""
            bot_reply = self.bot.reply(content, e_context.econtext['context'], system_prompt)
            logger.debug("[wxagent] reply: %s" % bot_reply)

            content = parse_markdown(bot_reply.content)
            reply = Reply()
            reply.type = ReplyType.TEXT
            reply.content = content

            reply = e_context.econtext['channel']._decorate_reply(e_context.econtext['context'], reply)
            e_context.econtext['channel']._send_reply(e_context.econtext.get('context', {}), reply)

            e_context.action = EventAction.BREAK_PASS

    def get_help_text(self, **kwargs):
        help_text = "AI 角色 回复"
        return help_text


def chat_service_openai_like(dataset_id: str, text: str):
    headers = {"Content-Type": "application/json",
               'Authorization': 'Bearer fastgpt-czbAiqKKse65hwwviZhwkgvyDEKE3aeB31Fx18oUsAGojyWQ672HdsWZi1E1C'}
    args = {
        "datasetId": dataset_id,
        "text": text,
        "limit": 2000,
        "similarity": 0.8,
        "searchMode": "mixedRecall",
        "usingReRank": False
    }
    response = requests.post("https://fastgpt.gkscrm.com/api/core/dataset/searchTest", headers=headers, json=args)
    logger.debug("[wxsop] response: %s" % response)
    logger.debug("[wxsop] response.status_code: %s" % response.status_code)
    logger.debug("[wxsop] response.json(): %s" % response.json())
    if response.status_code == 200:
        response_json = response.json()
        if "data" in response_json and "list" in response_json["data"]:
            return response_json["data"]["list"]
        else:
            return None
    return None
