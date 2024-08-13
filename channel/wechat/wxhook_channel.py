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
        return res.json(strict=False)
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


def wx_hook_request(path, data):
    # 添加字典
    # ports = {
    #     "wxid_77au928zeb2p12": 30001,
    #     "wxid_vxb2yrhrxsqs12": 30002,
    #     "wxid_l52egy9jtfu922": 30003,
    #     "wxid_0u13zxhwsxsu12": 30004,
    #     "wxid_wmz7m9nqrdg612": 30005,
    #     "bowen1116": 30006,
    #     "wxid_edc0mvp188ms22": 30007
    # }
    try:
        # path判断是不是/开头
        if not path.startswith("/"):
            path = "/" + path
        url = f"http://{conf().get('wx_hook_ip')}:{conf().get('wx_hook_port')}{path}"
        headers = {
            "Content-Type": "application/json",
        }
        res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
        logger.debug(f"[wx_hook] send message success, res: {res}")
        return res.json(strict=False)
    except Exception as e:
        logger.error(f"[wx_hook] send message failed, error: {e}")
        return None


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

    def wx_hook_request(self, path, data, private_ip, port):
        # 添加字典
        # ports = {
        #     "wxid_77au928zeb2p12": 30001,
        #     "wxid_vxb2yrhrxsqs12": 30002,
        #     "wxid_l52egy9jtfu922": 30003,
        #     "wxid_0u13zxhwsxsu12": 30004,
        #     "wxid_wmz7m9nqrdg612": 30005,
        #     "bowen1116": 30006,
        #     "wxid_edc0mvp188ms22": 30007
        # }
        try:
            # path判断是不是/开头
            if not path.startswith("/"):
                path = "/" + path
            url = f"http://{private_ip}:{port}{path}"
            headers = {
                "Content-Type": "application/json",
            }
            res = requests.post(url, headers=headers, json=data, timeout=(5, 10))
            logger.debug(f"[wx_hook] send message success, res: {res}")
            return res.json(strict=False)
        except Exception as e:
            logger.error(f"[wx_hook] send message failed, error: {e}")
            return None

    def getNickName(self, user_id, private_ip, port, group_id=""):
        if not self.nickNames.get(user_id):
            data = {
                "wxidorgid": user_id
            }
            res = self.wx_hook_request("/GetFriendOrChatroomDetailInfo", data, private_ip, port)
            if res:
                if "nickname" in res:
                    self.nickNames[user_id] = res.get("nickname")
                elif "gname" in res:
                    self.nickNames[user_id] = res.get("gname")
                else:
                    return ""
            else:
                logger.error(f"[wx_hook] get nickname failed, user_id={user_id}, group_id={group_id}")
                return ""
        return self.nickNames[user_id]

    def getGroup(self, group_id, private_ip, port):
        if not self.groups.get(group_id):
            data = {
                "wxidorgid": group_id
            }
            res = self.wx_hook_request("/GetFriendOrChatroomDetailInfo", data, private_ip, port)
            if res:
                self.groups[group_id] = res
        return self.groups[group_id]

    def getVoice(self, clientmsgid, length, fromgid, msgsvrid, private_ip, port):
        data = {
            "clientmsgid": clientmsgid,
            "length": length,
            "fromgid": fromgid,
            "msgsvrid": msgsvrid
        }

        res = self.wx_hook_request("/DownloadVoice", data, private_ip, port)
        return res

    def startup(self):

        # wxhook的时候不检测是否登录
        # while True:
        #     status = wx_hook_request("IsLoginStatus", {})
        #     #     判断status 不是 None
        #     if status is None or status.get("onlinestatus") != "3":
        #         logger.info(
        #             f"[wx_hook] check status: {status},please scan the QR code to login http://127.0.0.1:5000/checkStatus")
        #         sleep(5)
        #         continue
        #     else:
        #         break

        # wxhook的时候不设置回调
        # setCallBack = wx_hook_request("ConfigureMsgRecive",
        #                               {"isEnable": "1", "url": conf().get("wx_hook_callback_url")})
        # if setCallBack.get("ConfigureMsgRecive") == "1":
        #     logger.info(f"[wx_hook] set callback success")
        # else:
        #     logger.error(f"[wx_hook] set callback failed")

        # wxhook的时候不请求信息
        # selfInfo = wx_hook_request("/GetSelfLoginInfo", {})
        # self.name = selfInfo.get("nickname")
        # self.user_id = selfInfo.get("wxid")

        # 启动回调监听
        urls = (
            '/robot-api/webot/receiveChatBotMsg', 'channel.wechat.wxhook_channel.WxHookController'
        )
        app = web.application(urls, globals(), autoreload=False)
        port = conf().get("wx_hook_callback_port", 9007)
        web.httpserver.runsimple(app.wsgifunc(), ("0.0.0.0", port))

    def send(self, reply: Reply, context: Context):
        # logger.debug(f"[WxHookChannel] Context: {vars(Context)}")
        is_group = context["isgroup"]
        if reply.type == ReplyType.TEXT or reply.type == ReplyType.INFO or reply.type == ReplyType.ERROR or reply.type == ReplyType.TEXT_:
            # logger.debug(f"[wx_hook] send context: {context}")
            # logger.debug(f"[wx_hook] send context msg: {vars(context.kwargs['msg'])}")
            # logger.debug(f"[wx_hook] send context channel: {vars(context.kwargs['channel'])}")
            # logger.debug(f"[wx_hook] send context channel: {vars(context.kwargs['channel']['user_id'])}")
            private_ip = context["private_ip"]
            port = context["port"]
            data = {
                "wxid": context["receiver"],
                "msg": reply.content
            }
            res = self.wx_hook_request("/SendTextMsg", data, private_ip, port)
            context["is_success"] = res.get("SendTextMsg")
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
            res = self.wx_hook_request("/SendPicMsg", data, private_ip, port)
            context["is_success"] = res.get("SendPicMsg")
            if res.get("SendPicMsg") == "1":
                logger.info(f"[wx_hook] send url image success")
            else:
                logger.error(f"[wx_hook] send url image failed")

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
                logger.info(f"[wx_hook] send image success")
            else:
                logger.error(f"[wx_hook] send image failed")
        elif reply.type == ReplyType.LOCATION:
            data = {
                "wxid": context["receiver"],
                "msg": reply.content
            }
            res = self.wx_hook_request("/SendLocationMsg", data, private_ip, port)
            context["is_success"] = res.get("SendLocationMsg")
            if res.get("success") == "1":
                logger.info(f"[wx_hook] send location success")
            else:
                logger.error(f"[wx_hook] send location failed")
        elif reply.type == ReplyType.FILE:
            data = {
                "wxid": context["receiver"],
                "filepath": reply.content,
                "diyfilename": context["diyfilename"]
            }
            res = self.wx_hook_request("/SendFileMsg", data, private_ip, port)
            context["is_success"] = res.get("SendFileMsg")
            if res.get("success") == "1":
                logger.info(f"[wx_hook] send file success")
            else:
                logger.error(f"[wx_hook] send file failed")


class WxHookController:
    FAILED_MSG = '{"success": false}'
    SUCCESS_MSG = '{"success": true}'

    wxinfos = dict()
    servers = dict()

    def get_wxinfo_by_wxid(self, wxid):
        if not self.wxinfos.get(wxid):
            from app import db_storage
            wxinfo = db_storage.get_info_by_wxid(wxid)
            if wxinfo is None:
                return None
            else:
                self.wxinfos[wxid] = wxinfo
        return self.wxinfos.get(wxid)

    def get_serverinfo(self, server_id):
        if not self.servers.get(server_id):
            from app import db_storage
            server = db_storage.get_server_by_id(server_id)
            if server is None:
                return None
            else:
                self.servers[server_id] = server
        return self.servers.get(server_id)

    def POST(self):
        data = json.loads(web.data().decode("utf-8"), strict=False)
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
        # 更正连接信息
        wxinfo = self.get_wxinfo_by_wxid(data.get("selfwxid"))
        logger.debug(f"[wx_hook] --------------------api_base-----------------, msg={wxinfo}")

        channel.user_id = data.get("selfwxid")

        if wxinfo is not None:
            channel.name = wxinfo['nickname']
            server = self.get_serverinfo(wxinfo['server_id'])
            if server is not None:
                channel.wx_hook_ip = server['private_ip']
                channel.wx_hook_port = wxinfo['port']
                channel.wx_hook_admin_port = server['admin_port']
        # 循环处理每一条消息 data.get("msglist")
        for msg in data.get("msglist"):

            if "cmdId" in msg:
                return "this is a cmd message"

            selfwxid = ""

            # 过滤自己的消息
            if data.get("selfwxid") != "":
                selfwxid = data.get("selfwxid")

            if selfwxid == "":
                logger.debug(f"[wx_hook] selfwxid is empty")
                continue

            if selfwxid == msg.get("fromid"):
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

            wx_hook_msg = WxHookMessage(msg, channel, selfwxid, server['private_ip'], wxinfo['port'])

            logger.debug("[wx_hook] wx_hook_msg message: {}".format(wx_hook_msg))

            context = channel._compose_context(wx_hook_msg.ctype, wx_hook_msg.content, isgroup=wx_hook_msg.is_group,
                                               msg=wx_hook_msg)

            if wxinfo and wxinfo['api_base']:
                context['open_ai_api_base'] = wxinfo['api_base']
                context['open_ai_api_key'] = wxinfo['api_key']
                context['wxid'] = wxinfo['wxid']
                context['private_ip'] = server['private_ip']
                context['port'] = wxinfo['port']
                logger.debug(f"[wx_hook] open_ai_api_base, msg={wxinfo['api_base']}")
                logger.debug(f"[wx_hook] open_ai_api_key, msg={wxinfo['api_key']}")

            logger.debug(f"[wx_hook] context is {context}")
            if context:
                logger.debug(f"[wx_hook] context session_id is {context['session_id']}")
                channel.produce(context)

        return "success"
