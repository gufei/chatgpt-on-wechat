# encoding:utf-8
import json
import time

import openai
import openai.error
import requests
from bot.bot import Bot
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.openai.open_ai_image import OpenAIImage
from bot.session_manager import SessionManager
from bridge.context import ContextType
from bridge.reply import Reply, ReplyType
from common.log import logger
from common.token_bucket import TokenBucket
from config import conf, load_config


# OpenAI对话模型API (可用)
class OpenaiBot(Bot, OpenAIImage):
    def __init__(self,
                 open_ai_api_base: str,
                 open_ai_api_key: str,
                 model: str = "gpt-4o"):
        super().__init__()
        # set the default api_key
        # openai.api_key = conf().get("open_voice_api_key")
        # if conf().get("open_voice_api_base"):
        #     openai.api_base = conf().get("open_voice_api_base")
        self.open_ai_api_base = open_ai_api_base
        self.open_ai_api_key = open_ai_api_key
        proxy = conf().get("proxy")
        if proxy:
            openai.proxy = proxy
        if conf().get("rate_limit_chatgpt"):
            self.tb4chatgpt = TokenBucket(conf().get("rate_limit_chatgpt", 20))

        # self.sessions = SessionManager(ChatGPTSession, model=conf().get("model") or "gpt-3.5-turbo")
        self.args = {
            "model": model,  # 对话模型的名称
            "stream": False,  # 是否开启流模式
        }

    def reply(self, query, context=None):
        # acquire reply content
        if context.type == ContextType.TEXT:
            logger.info("[CHATGPT] query={}".format(query))

            reply = None

            new_args = self.args.copy()
            new_args["messages"] = [{
                "role": "user",
                "content": query
            }]

            reply_content = self.chat_service_openai_like(new_args)
            reply = Reply(
                ReplyType.TEXT,
                reply_content,
            )
            return reply

        elif context.type == ContextType.IMAGE_CREATE:
            ok, retstring = self.create_img(query, 0)
            reply = None
            if ok:
                reply = Reply(ReplyType.IMAGE_URL, retstring)
            else:
                reply = Reply(ReplyType.ERROR, retstring)
            return reply
        else:
            reply = Reply(ReplyType.ERROR, "Bot不支持处理{}类型的消息".format(context.type))
            return reply

    def chat_service_openai_like(self, args=None):
        headers = {"Content-Type": "application/json", 'Authorization': 'Bearer ' + self.open_ai_api_key}

        logger.debug("[wxsop] self.open_ai_api_base: %s" % self.open_ai_api_base)
        logger.debug("[wxsop] headers: %s" % headers)
        logger.debug("[wxsop] args: %s" % args)

        response = requests.post(self.open_ai_api_base, headers=headers, json=args)
        logger.debug("[wxsop] response: %s" % response)
        if response.status_code == 200:
            response_json = response.json()
            return response_json["choices"][0]["message"]["content"]
        return None
