# encoding:utf-8
import json
import re
import time
import urllib.parse
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
from lib.usage_token import usage_storage


# OpenAI对话模型API (可用)
class ChatGPTBot(Bot, OpenAIImage):
    def __init__(self):
        super().__init__()
        # set the default api_key
        openai.api_key = conf().get("open_ai_api_key")
        if conf().get("open_ai_api_base"):
            openai.api_base = conf().get("open_ai_api_base")
        proxy = conf().get("proxy")
        if proxy:
            openai.proxy = proxy
        if conf().get("rate_limit_chatgpt"):
            self.tb4chatgpt = TokenBucket(conf().get("rate_limit_chatgpt", 20))

        self.sessions = SessionManager(ChatGPTSession, model=conf().get("model") or "gpt-3.5-turbo")
        self.args = {
            "model": conf().get("model") or "gpt-3.5-turbo",  # 对话模型的名称
            "temperature": conf().get("temperature", 0.9),  # 值在[0,1]之间，越大表示回复越具有不确定性
            # "max_tokens":4096,  # 回复最大的字符数
            "top_p": conf().get("top_p", 1),
            "frequency_penalty": conf().get("frequency_penalty", 0.0),  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "presence_penalty": conf().get("presence_penalty", 0.0),  # [-2,2]之间，该值越大则更倾向于产生不同的内容
            "request_timeout": conf().get("request_timeout", None),  # 请求超时时间，openai接口默认设置为600，对于难问题一般需要较长时间
            "timeout": conf().get("request_timeout", None),  # 重试超时时间，在这个时间内，将会自动重试
        }

    def reply(self, query, context=None):
        # acquire reply content
        if context.type == ContextType.TEXT:
            logger.info("[CHATGPT] query={}".format(query))

            session_id = "chatId-{}".format(context["wxid"] + "_" + format(context["session_id"]))

            reply = None
            clear_memory_commands = conf().get("clear_memory_commands", ["#清除记忆"])
            if query in clear_memory_commands:
                self.sessions.clear_session(session_id)
                reply = Reply(ReplyType.INFO, "记忆已清除")
            elif query == "#清除所有":
                self.sessions.clear_all_session()
                reply = Reply(ReplyType.INFO, "所有人记忆已清除")
            elif query == "#更新配置":
                load_config()
                reply = Reply(ReplyType.INFO, "配置已更新")
            if reply:
                return reply
            session = self.sessions.session_query(query, session_id)
            logger.debug("[CHATGPT] session query={}".format(session.messages))

            if context.get("open_ai_api_key"):
                api_key = context.get("open_ai_api_key")
            if context.get("open_ai_api_base"):
                api_base = context.get("open_ai_api_base")
            if context.get("api_key"):
                api_key = context.get("api_key")

            # model = context.get("gpt_model")
            # new_args = None
            # if model:
            #     new_args = self.args.copy()
            #     new_args["model"] = model
            # if context.get('stream'):
            #     # reply in stream
            #     return self.reply_text_stream(query, new_query, session_id)

            new_args = self.args.copy()

            new_args['api_base'] = api_base
            sop_unmatched = context.get('sop_unmatched', None)
            if "fastgpt" in api_base or "fastgpt" in api_key:
                new_args["chatId"] = session.session_id
                new_args["detail"] = True
                # new_args["messages"] = [session.messages[-1]]
                if context.get("open_ai_model"):
                    new_args['variables'] = {
                        "model": context.get("open_ai_model", "gpt-4o-mini")
                    }
                if sop_unmatched:
                    if len(session.messages) > 0:
                        messages = [{
                            "role": "user",
                            "content": f"""{session.messages[-1].get("content", "")}

# 回复要求
在回复内容的最后，需要引导用户回到指定话题：{sop_unmatched}""",
                    }]
                    else:
                        messages = [{
                            "role": "user",
                            "content": f"""# 回复要求
在回复内容的最后，需要引导用户回到指定话题：{sop_unmatched}"""
                        }]
                else:
                    messages = session.messages[-1]
                new_args["messages"] = messages
            else:
                if context.get("open_ai_model"):
                    new_args['model'] = context.get("open_ai_model", "gpt-4o-mini")
                # new_args["messages"] = session.messages
                if len(session.messages) > 0:
                    messages = session.messages
                    messages.insert(0, {
                        "role": "system",
                        "content": f"""# 回复要求
在回复内容的最后，需要引导用户回到指定话题：{sop_unmatched}"""
                    })
                else:
                    messages = session.messages
                new_args["messages"] = messages

            reply_content = self.reply_text(session, api_key, args=new_args, context=context)
            logger.debug(
                "[CHATGPT] new_query={}, session_id={}, reply_cont={}, completion_tokens={}".format(
                    new_args,
                    session.session_id,
                    reply_content["content"],
                    reply_content["completion_tokens"],
                )
            )
            if reply_content["completion_tokens"] == 0 and len(reply_content["content"]) > 0:
                reply = Reply(ReplyType.ERROR, reply_content["content"])
            elif reply_content["completion_tokens"] > 0:
                if is_json_array(reply_content["content"]):
                    dict_data = json.loads(reply_content["content"])
                    session_content = ""
                    for c in dict_data:
                        if c.get("type") == "FILE" or c.get("type") == "IMAGE_URL" or c.get("type") == "IMAGE" or c.get("type") == "VIDEO_URL" or c.get("type") == "VIDEO":
                            session_content += f'![]({c.get("content", "")})' + "\n\n"
                        else:
                            session_content += c.get("content", "") + "\n\n"
                else:
                    session_content = reply_content["content"]
                self.sessions.session_reply(session_content, session.session_id, reply_content["total_tokens"])
                reply = Reply(ReplyType.TEXT, reply_content["content"])
            else:
                reply = Reply(ReplyType.ERROR, reply_content["content"])
                logger.debug("[CHATGPT] reply {} used 0 tokens.".format(reply_content))
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

    def reply_text(self, session: ChatGPTSession, api_key=None, args=None, retry_count=0, context=None) -> dict:
        """
        call openai's ChatCompletion to get the answer
        :param session: a conversation session
        :param session_id: session id
        :param retry_count: retry count
        :return: {}
        """
        try:
            if conf().get("rate_limit_chatgpt") and not self.tb4chatgpt.get_token():
                raise openai.error.RateLimitError("RateLimitError: rate limit exceeded")
            # if api_key == None, the default openai.api_key will be used
            if args is None:
                args = self.args

            # response = openai.ChatCompletion.create(api_key=api_key, messages=session.messages, **args)
            # args["messages"] = [session.messages[-1]]
            # logger.debug("[CHATGPT] args={}".format(args))
            headers = {"Content-Type": "application/json", 'Authorization': 'Bearer ' + api_key}
            api_base = args['api_base']
            # 清理不能传的参数
            if "api_base" in args:
                del args["api_base"]
            if "request_timeout" in args:
                del args["request_timeout"]
            if "timeout" in args:
                del args["timeout"]
            logger.debug("[CHATGPT] api_base={}".format(api_base))
            logger.debug("[CHATGPT] api_key={}".format(api_key))
            # logger.debug("[CHATGPT] jsondata={}".format(jsondata))
            response = requests.post(api_base + "/chat/completions", headers=headers, json=args)
            logger.debug("[CHATGPT] response={}".format(response))
            response_json = response.json()

            if conf().get("channel_type", "wx_hook") == "whatsapp":
                bot_type = 3
            elif conf().get("channel_type", "wx_hook") == "wework_hook":
                bot_type = 4
            else:
                bot_type = 1
            usage_storage(bot_type, context["wxid"], context["session_id"], 1, 0, args, response_json, context["organization_id"])

            content = parse_markdown(response_json["choices"][0]["message"]["content"])

            logger.info("[ChatGPT] reply={}, response_json={}".format(response_json["choices"][0]['message']['content'], response_json))
            return {
                "total_tokens": response_json["usage"]["total_tokens"],
                "completion_tokens": response_json["usage"]["completion_tokens"],
                "content": content,
            }
        except Exception as e:
            need_retry = retry_count < 2
            result = {"completion_tokens": 0, "content": "我现在有点累了，等会再来吧"}
            if isinstance(e, openai.error.RateLimitError):
                logger.warn("[CHATGPT] RateLimitError: {}".format(e))
                result["content"] = "提问太快啦，请休息一下再问我吧"
                if need_retry:
                    time.sleep(20)
            elif isinstance(e, openai.error.Timeout):
                logger.warn("[CHATGPT] Timeout: {}".format(e))
                result["content"] = "我没有收到你的消息"
                if need_retry:
                    time.sleep(5)
            elif isinstance(e, openai.error.APIError):
                logger.warn("[CHATGPT] Bad Gateway: {}".format(e))
                result["content"] = "请再问我一次"
                if need_retry:
                    time.sleep(10)
            elif isinstance(e, openai.error.APIConnectionError):
                logger.warn("[CHATGPT] APIConnectionError: {}".format(e))
                result["content"] = "我连接不到你的网络"
                if need_retry:
                    time.sleep(5)
            else:
                logger.exception("[CHATGPT] Exception: {}".format(e))
                need_retry = False
                self.sessions.clear_session(session.session_id)

            if need_retry:
                logger.warn("[CHATGPT] 第{}次重试".format(retry_count + 1))
                return self.reply_text(session, api_key, args, retry_count + 1, context)
            else:
                return result


def parse_markdown(input_text):
    # 当字符串以[开头时跳过
    if is_json_array(input_text):
        return input_text
    # 定义正则表达式来匹配Markdown格式的图片
    image_pattern = re.compile(r'!?\[(.*?)\]\((.*?)\)')
    # 定义正则表达式来匹配两个以上的换行符
    split_pattern = re.compile(r'\n{2,}')

    # 用来存储解析后的结果
    result = []

    # 用来记录当前处理的位置
    last_pos = 0

    # 迭代匹配到的图片
    for match in image_pattern.finditer(input_text):
        # 获取匹配到的图片的前一段文本
        if match.start() > last_pos:
            text_segment = input_text[last_pos:match.start()].strip()
            if text_segment:
                # 将文本按两个以上的换行符进行分段
                segments = split_pattern.split(text_segment)
                # 处理每一段
                for segment in segments:
                    result.append({
                        "type": "TEXT",
                        "content": segment
                    })

        # 获取图片信息
        # alt_text = match.group(1)
        image_url = match.group(2)
        image_filename = image_url.split('/')[-1]

        if image_url.lower().endswith(('.mp4', '.mov', '.avi', '.wmv', '.mpg', '.mpeg', '.jpg', '.jpeg', '.png', '.gif', '.webp', '.heic', '.heif', '.wav')):
            result.append({
                "type": "FILE",
                "content": image_url,
                "diyfilename": urllib.parse.unquote(image_filename)
            })
        else:
            result.append({
                "type": "TEXT",
                "content": image_url
            })

        # 更新当前处理的位置
        last_pos = match.end()

    # 获取最后一段文本
    if last_pos < len(input_text):
        text_segment = input_text[last_pos:].strip()
        if text_segment:
            segments = split_pattern.split(text_segment)
            # 处理每一段
            for segment in segments:
                result.append({
                    "type": "TEXT",
                    "content": segment
                })

    return json.dumps(result, ensure_ascii=False, indent=4)

def is_json_array(input_text):
    try:
        data = json.loads(input_text)
        if isinstance(data, list):
            return True
        return False
    except json.JSONDecodeError:
        return False

class AzureChatGPTBot(ChatGPTBot):
    def __init__(self):
        super().__init__()
        openai.api_type = "azure"
        openai.api_version = conf().get("azure_api_version", "2023-06-01-preview")
        self.args["deployment_id"] = conf().get("azure_deployment_id")

    def create_img(self, query, retry_count=0, api_key=None):
        api_version = "2022-08-03-preview"
        url = "{}dalle/text-to-image?api-version={}".format(openai.api_base, api_version)
        api_key = api_key or openai.api_key
        headers = {"api-key": api_key, "Content-Type": "application/json"}
        try:
            body = {"caption": query, "resolution": conf().get("image_create_size", "256x256")}
            submission = requests.post(url, headers=headers, json=body)
            operation_location = submission.headers["Operation-Location"]
            retry_after = submission.headers["Retry-after"]
            status = ""
            image_url = ""
            while status != "Succeeded":
                logger.info("waiting for image create..., " + status + ",retry after " + retry_after + " seconds")
                time.sleep(int(retry_after))
                response = requests.get(operation_location, headers=headers)
                status = response.json()["status"]
            image_url = response.json()["result"]["contentUrl"]
            return True, image_url
        except Exception as e:
            logger.error("create image error: {}".format(e))
            return False, "图片生成失败"
