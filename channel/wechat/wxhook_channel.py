import json
from time import sleep

import requests
import web

from bridge.context import Context, ContextType
from channel.chat_channel import ChatChannel
from channel.wechat.wxhook_message import WxHookMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from common.singleton import singleton
from config import conf
from bridge.reply import Reply, ReplyType


def wx_hook_admin_request(path, data):
    try:
        if not path.startswith("/"):
            path = "/" + path
        url = f"http://{conf().get('wx_hook_ip')}:{conf().get('wx_hook_admin_port')}{path}"
        headers = {
            "Content-Type": "application/json",
        }
        res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
        return res.json()
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


def wx_hook_request(path, data):
    try:
        # path判断是不是/开头
        if not path.startswith("/"):
            path = "/" + path
        url = f"http://{conf().get('wx_hook_ip')}:{conf().get('wx_hook_port')}{path}"
        headers = {
            "Content-Type": "application/json",
        }
        res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
        return res.json()
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


@singleton
class WxHookChannel(ChatChannel):
    wx_hook_ip = conf().get('wx_hook_ip')
    wx_hook_port = conf().get('wx_hook_port')
    wx_hook_admin_port = conf().get('wx_hook_admin_port')
    wx_hook_callback_port = conf().get('wx_hook_callback_port')

    groups = dict()
    nickNames = dict()
    users = dict()

    def __init__(self):
        super().__init__()
        # 历史消息id暂存，用于幂等控制
        self.receivedMsgs = ExpiredDict(60 * 60 * 7.1)
        logger.info("[WxHook] ip={}, port={} admin_port={} callback_port={}".format(
            self.wx_hook_ip, self.wx_hook_port, self.wx_hook_admin_port, self.wx_hook_callback_port))

    def getNickName(self, user_id, group_id=""):
        if not self.nickNames.get(group_id + "_" + user_id):
            if group_id == "":
                data = {"wxid": user_id}
            else:
                data = {
                    "gid": group_id,
                    "wxid": user_id
                }
            res = wx_hook_request("/GetChatroomMemberDetailInfo", data)
            if res:
                self.nickNames[group_id + "_" + user_id] = res.get("nickname")
        return self.nickNames[group_id + "_" + user_id]

    def getGroup(self, group_id):
        if not self.groups.get(group_id):
            data = {
                "wxidorgid": group_id
            }
            res = wx_hook_request("/GetFriendOrChatroomDetailInfo", data)
            if res:
                self.groups[group_id] = res
        return self.groups[group_id]

    def getVoice(self, clientmsgid, length, fromgid, msgsvrid):
        data = {
            "clientmsgid": clientmsgid,
            "length": length,
            "fromgid": fromgid,
            "msgsvrid": msgsvrid
        }

        res = wx_hook_request("/DownloadVoice", data)
        return res

    def startup(self):
        while True:
            status = wx_hook_request("IsLoginStatus", {})
            #     判断status 不是 None
            if status is None or status.get("onlinestatus") != "3":
                logger.info(
                    f"[wx_hook] check status: {status},please scan the QR code to login http://127.0.0.1:5000/checkStatus")
                sleep(5)
                continue
            else:
                break

        # 设置回调
        setCallBack = wx_hook_request("ConfigureMsgRecive",
                                      {"isEnable": "1", "url": conf().get("wx_hook_callback_url")})
        if setCallBack.get("ConfigureMsgRecive") == "1":
            logger.info(f"[wx_hook] set callback success")
        else:
            logger.error(f"[wx_hook] set callback failed")

        selfInfo = wx_hook_request("/GetSelfLoginInfo", {})
        self.name = selfInfo.get("nickname")
        self.user_id = selfInfo.get("wxid")
        urls = (
            '/robot-api/webot/receiveChatBotMsg', 'channel.wechat.wxhook_channel.WxHookController'
        )
        app = web.application(urls, globals(), autoreload=False)
        port = conf().get("wx_hook_callback_port", 9001)
        web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", port))

    def send(self, reply: Reply, context: Context):
        is_group = context["isgroup"]
        if reply.type == ReplyType.TEXT or reply.type == ReplyType.INFO or reply.type == ReplyType.ERROR or reply.type == ReplyType.TEXT_:
            data = {
                "wxid": context["receiver"],
                "msg": reply.content
            }
            res = wx_hook_request("/SendTextMsg", data)
            if res.get("SendTextMsg") == "1":
                logger.info(f"[wx_hook] send message success")
            else:
                logger.error(f"[wx_hook] send message failed")
        elif reply.type == ReplyType.IMAGE_URL:  # 从网络下载图片
            data = {
                "wxid": context["receiver"],
                "picpath": reply.content,
                "diyfilename": "1.jpg"
            }
            logger.debug(f"[wx_hook] send image data: {data}")
            res = wx_hook_request("/SendPicMsg", data)
            if res.get("SendPicMsg") == "1":
                logger.info(f"[wx_hook] send url image success")
            else:
                logger.error(f"[wx_hook] send url image failed")
        elif reply.type == ReplyType.IMAGE:
            data = {
                "wxid": context["receiver"],
                "picpath": "C:\\Users\\Administrator\\Desktop\\files\\" + reply.content
            }
            res = wx_hook_request("/SendPicMsg", data)
            if res.get("SendPicMsg") == "1":
                logger.info(f"[wx_hook] send image success")
            else:
                logger.error(f"[wx_hook] send image failed")
        elif reply.type == ReplyType.FILE:
            data = {
                "wxid": context["receiver"],
                "filepath": "C:\\Users\\Administrator\\Desktop\\files\\" + reply.content
            }
            res = wx_hook_request("/SendFileMsg", data)
            if res.get("success") == "1":
                logger.info(f"[wx_hook] send file success")
            else:
                logger.error(f"[wx_hook] send file failed")


class WxHookController:
    FAILED_MSG = '{"success": false}'
    SUCCESS_MSG = '{"success": true}'

    def POST(self):
        data = json.loads(web.data().decode("utf-8"))
        logger.info(f"[wx_hook] receive request: {data}")

        # 只接收 30001、30002、30003、30004、30005 和配置的 端口的消息
        if data.get("ServerPort") not in ["30001", "30002", "30003", "30004", "30005", conf().get("wx_hook_port")]:
            logger.debug(f"[wx_hook] not a specified port, port={data.get('port')}")
            return "not a specified port"

        # 只处理接收消息
        if data.get("sendorrecv") != "2":
            logger.debug(f"[wx_hook] not a receive message")
            return "not a receive message"

        # 没有消息
        if data.get("msgnumber") == 0:
            logger.debug(f"[wx_hook] no message")
            return "no message"

        channel = WxHookChannel()

        # 循环处理每一条消息 data.get("msglist")
        for msg in data.get("msglist"):
            # 过滤自己的消息
            if data.get("selfwxid") == msg.get("fromid"):
                logger.debug(f"[wx_hook] self message filtered, fromid={msg.get('fromid')}")
                continue

            # 只处理文本类型的消息
            if msg.get("msgtype") not in ["1", "34"]:
                logger.debug(f"[wx_hook] not a text message, msgtype={msg.get('msgtype')}")
                continue

            if channel.receivedMsgs.get(msg.get("msgsvrid")):
                logger.warning(f"[wx_hook] repeat msg filtered, msgsvrid={msg.get('msgsvrid')}")
                logger.debug(f"[wx_hook] repeat msg filtered, msg={msg}")
                return self.SUCCESS_MSG
            channel.receivedMsgs[msg.get("msgsvrid")] = True

            wx_hook_msg = WxHookMessage(msg, channel, data.get("selfwxid"))

            logger.debug("[wx_hook] wx_hook_msg message: {}".format(wx_hook_msg))

            context = channel._compose_context(wx_hook_msg.ctype, wx_hook_msg.content, isgroup=wx_hook_msg.is_group,
                                               msg=wx_hook_msg)

            logger.debug(f"[wx_hook] context is {context}")
            if context:
                logger.debug(f"[wx_hook] context session_id is {context['session_id']}")
                channel.produce(context)

        return "success"
