import json
import urllib.parse
import requests
import web
import platform
import os
import sys

from app import redis_conn, db_storage
from bridge.context import Context, ContextType
from channel.chat_channel import ChatChannel
from channel.wechat.telegram_message import TelegramMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from config import conf
from bridge.reply import Reply, ReplyType

from telegram import Update
from telegram.ext import filters, MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, InlineQueryHandler


class TelegramChannel(ChatChannel):
    telegram_token = conf().get('telegram_token')
    telegram_id = conf().get('telegram_id')
    telegram_name = conf().get('telegram_name')

    FAILED_MSG = '{"success": false}'
    SUCCESS_MSG = '{"success": true}'


    def __init__(self):
        super().__init__()
        logger.info("[TGHook] token={}".format(self.telegram_token))
        self.get_tg_info()
        self.tg_info = {}

    def set_proxy(self):
        system = platform.system()  # 获取操作系统名字
        # print(system)
        if system == 'Darwin':
            # 处于开发环境
            os.environ["http_proxy"] = "http://127.0.0.1:7890"
            os.environ["https_proxy"] = "http://127.0.0.1:7890"
            os.environ["all_proxy"] = "http://127.0.0.1:7890"
        elif system == 'Linux':
            # 处于生产环境
            pass
        elif system == 'Windows':
            pass
        else:
            sys.exit('Unknown system.')


    def get_tg_info(self):
        self.tg_info = {
            "default": {
                "api_base": "http://fastgpt.ascrm.cn/api/v1",
                "api_key": "fastgpt-itoLce59lwO5r06Zhli2AJ2CtQUiPeoVf9k3PGPPM9jrGqbieWMLd4U",
            }
        }
        logger.info(f"初始化账号数据完成")


    def startup(self):
        self.set_proxy()

        # 创建机器人实例的，在这里放入 token
        application = ApplicationBuilder().token(self.telegram_token).build()

        application.add_handler(MessageHandler(filters.Mention(self.telegram_id), self.on_mention))

        # (~filters.COMMAND)  filters 是过滤，~ 是取反，就是所有非指令的消息
        application.add_handler(MessageHandler((~filters.COMMAND), self.on_message))

        # 启动，直到按 Ctrl-C
        application.run_polling(allowed_updates=Update.ALL_TYPES)

    def send(self, reply: Reply, context: Context):
        # logger.debug(f"[TelegramChannel] Context: {vars(Context)}")
        private_ip = context["private_ip"]
        port = context["port"]
        is_group = context["isgroup"]
        if reply.type == ReplyType.TEXT or reply.type == ReplyType.INFO or reply.type == ReplyType.ERROR or reply.type == ReplyType.TEXT_:
            if is_group and False:
                data = {
                    "type": "57",
                    "towxid": context["receiver"],
                    "xml": "<appmsg appid=\"\" sdkver=\"0\"><title>" + reply.content + "</title><des></des><action>view</action><type>57</type><showtype>0</showtype><content></content><url></url><dataurl></dataurl><lowurl></lowurl><lowdataurl></lowdataurl><recorditem></recorditem><thumburl></thumburl><messageaction></messageaction><laninfo></laninfo><refermsg><type>1</type><svrid>" +
                           context['cmd_msgsvrid'] + "</svrid><fromusr>" + context[
                               'wx_hook_msg'].to_user_id + "</fromusr><chatusr>" + context[
                               'wx_hook_msg'].actual_user_id + "</chatusr><displayname>" + context[
                               'wx_hook_msg'].actual_user_nickname + "</displayname><msgsource /><content>" + context[
                               'wx_hook_msg'].content + "</content></refermsg><extinfo></extinfo><sourceusername></sourceusername><sourcedisplayname></sourcedisplayname><commenturl></commenturl><appattach><totallen>0</totallen><attachid></attachid><emoticonmd5></emoticonmd5><fileext></fileext><aeskey></aeskey></appattach><weappinfo><pagepath></pagepath><username></username><appid></appid><appservicetype>0</appservicetype></weappinfo><websearch /></appmsg>",
                }
                res = self.wx_hook_request("/FowardXMLMsg", data, private_ip, port)
                context["is_success"] = res.get("FowardXMLMsg")
                if res.get("FowardXMLMsg") == "1":
                    logger.info(f"[telegram] send FowardXMLMsg message success")
                else:
                    logger.error(f"[telegram] send FowardXMLMsg message failed")
            else:
                if "@openim" in context["receiver"]:
                    data = {
                        "wxidorgid": context["receiver"],
                        "msg": reply.content
                    }
                    res = self.wx_hook_request("/SendTextMsg_NoSrc", data, private_ip, port)
                    context["is_success"] = res.get("SendTextMsg_NoSrc")
                    if res.get("SendTextMsg_NoSrc") == "1":
                        logger.info(f"[telegram] send message SendTextMsg_NoSrc success")
                else:
                    data = {
                        "wxid": context["receiver"],
                        "msg": reply.content
                    }
                    res = self.wx_hook_request("/SendTextMsg", data, private_ip, port)
                    context["is_success"] = res.get("SendTextMsg")
                    if res.get("SendTextMsg") == "1":
                        logger.info(f"[telegram] send message success")
                    else:
                        logger.error(f"[telegram] send message failed")
        elif reply.type == ReplyType.IMAGE_URL:  # 从网络下载图片
            data = {
                "wxid": context["receiver"],
                "picpath": reply.content,
                "diyfilename": "1.jpg"
            }
            logger.debug(f"[telegram] send image data: {data}")
            res = self.wx_hook_request("/SendPicMsg", data, private_ip, port)
            context["is_success"] = res.get("SendPicMsg")
            if res.get("SendPicMsg") == "1":
                logger.info(f"[telegram] send url image success")
            else:
                logger.error(f"[telegram] send url image failed")

            # data = {
            #     "wxid": context["receiver"],
            #     "msg": reply.content
            # }
            # # 补偿发送图片链接
            # wx_hook_request("/SendTextMsg", data)
        elif reply.type == ReplyType.IMAGE:
            data = {
                "wxid": context["receiver"],
                "picpath": "C:\\Users\\Administrator\\Desktop\\files\\" + reply.content
            }
            res = self.wx_hook_request("/SendPicMsg", data, private_ip, port)
            context["is_success"] = res.get("SendPicMsg")
            if res.get("SendPicMsg") == "1":
                logger.info(f"[telegram] send image success")
            else:
                logger.error(f"[telegram] send image failed")
        elif reply.type == ReplyType.LOCATION:
            data = {
                "wxid": context["receiver"],
                "msg": reply.content
            }
            res = self.wx_hook_request("/SendLocationMsg", data, private_ip, port)
            context["is_success"] = res.get("SendLocationMsg")
            if res.get("SendLocationMsg") == "1":
                logger.info(f"[telegram] send location success")
            else:
                logger.error(f"[telegram] send location failed")
        elif reply.type == ReplyType.FILE:
            decoded_str = urllib.parse.unquote(context["diyfilename"])
            data = {
                "wxid": context["receiver"],
                "filepath": reply.content,
                "diyfilename": decoded_str
            }
            res = self.wx_hook_request("/SendFileMsg", data, private_ip, port)

            context["is_success"] = res.get("SendFileMsg")
            if res.get("SendFileMsg") == "1":
                logger.info(f"[telegram] send file success")
            else:
                logger.error(f"[telegram] send file failed")

    def get_context_type(self, update: Update):
        entities = update.message.entities
        for entity in entities:
            logger.error(f"entity={entity}")

        return ContextType.TEXT

    async def on_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.warning(f"on_message: update.message={update.message.from_user}")

        self.get_context_type(update)

        extra = {
            "to_user_id": self.telegram_id,
            "to_user_nickname": self.telegram_name,
        }
        msg = TelegramMessage(update, extra)
        context = super()._compose_context(ContextType.TEXT, update.message.text, isgroup=False,
                                           msg=msg)

        if context is None:
            return self.FAILED_MSG

        # 增加需要的context
        context['update'] = update

        # 获取wxinfo账号信息

        wxinfo = db_storage.get_info_by_wxid()
        context['open_ai_api_base'] = wxinfo['api_base']
        context['open_ai_api_key'] = wxinfo['api_key']
        context['organization_id'] = wxinfo['organization_id']

        logger.debug(f"[telegram] context is {context}")
        if context:
            logger.debug(f"[telegram] context session_id is {context['session_id']}")
            self.produce(context)

        # await context.bot.send_message(chat_id=update.effective_chat.id, text="你有什么问题，可以随时问我哦……")

    async def on_mention(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        logger.warning(f"on_mention: text={update.message.text}")

        # 判断是否有 @ 事件
        entities = update.message.entities
        logger.error(f"entities={entities} len={len(entities)}")
        for entity in entities:
            logger.error(f"entity={entity}")
            if entity.type == 'mention':
                reply_text = f"你好，@{update.effective_user.username}！有什么可以帮你的？直接发送问题我会给你解答"
                await update.message.reply_text(reply_text)