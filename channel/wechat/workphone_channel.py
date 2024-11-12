import json
import threading

import requests
from google.protobuf.json_format import ParseDict, MessageToDict

from app import redis_conn
from bridge.context import Context, ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_channel import ChatChannel
from channel.wechat.workphone_message import WorkPhoneMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from common.singleton import singleton
from lib.wsclient import WebSocketClient
from workphone.DeviceAuthRsp_pb2 import DeviceAuthRspMessage
from workphone.FriendTalkNotice_pb2 import FriendTalkNoticeMessage
from workphone.TalkToFriendTask_pb2 import TalkToFriendTaskMessage
from workphone.TransportMessage_pb2 import EnumContentType, TransportMessage, EnumMsgType

from google.protobuf.any_pb2 import Any


@singleton
class WorkPhoneChannel(ChatChannel):

    wx_info = dict()

    def __init__(self):
        super().__init__()
        self.receivedMsgs = ExpiredDict(60 * 60)
        self.get_wx_info()

    def get_wx_info(self):
        logger.info(f"初始化账号数据")
        url = "http://chat.gkscrm.com:13086/pc/GetWeChatsReq?id=13"
        response = requests.request("POST", url)

        if response.status_code != 200:
            logger.error("Error while fetching the wechats")

        res = response.json()

        if res.get('code') != 0:
            logger.error('Error while fetching the wechats')

        for wx_info in res['data']:

            self.wx_info[wx_info['wechatid']] = wx_info

            redis_conn.hset('workphone_wechat_info', wx_info['wechatid'], json.dumps(wx_info))

            url = "http://chat.gkscrm.com:13086/pc/GetWechatFriendList?cid=" + str(wx_info['cid']) + "&wechatid=" + wx_info[
                'wechatid']
            response = requests.request("POST", url)
            if response.status_code != 200:
                logger.error("Error while fetching the friends")
                continue
            res = response.json()
            for friend in res['data']:
                if friend['type'] == 0:
                    redis_conn.hset('workphone_contact_info_' + wx_info['wechatid'], friend['friendid'],
                                    json.dumps(friend))
                elif friend['type'] == 1:
                    redis_conn.hset('workphone_group_info_' + wx_info['wechatid'], friend['friendid'],
                                    json.dumps(friend))

            wx = redis_conn.hget('workphone_wechat_info',wx_info['wechatid'])

        logger.info(f"初始化账号数据完成")



    def startup(self):
        self.wsCli = WebSocketClient("ws://chat.gkscrm.com:13088")
        self.wsCli.start()
        self.wsCli.ws.on_message = self.on_message

    def on_device_auth(self, ws, msg_dict):
        """
        认证注册回调
        """
        msg = DeviceAuthRspMessage()
        msg = ParseDict(msg_dict, msg)
        self.access_token = msg.AccessToken
        logger.info(f'认证完成 AccessToken:{self.access_token}')

        # 构造发送心跳包
        heart_beat_req = {
            "Id": 1001,
            "MsgType": "HeartBeatReq",
            "AccessToken": self.access_token,
            "Content": {
                "token": self.access_token
            }
        }

        thread = threading.Thread(
            target=self.wsCli.send_heart_beat_event, args=(30, self.wsCli.heart_beat_event, json.dumps(heart_beat_req)))
        thread.daemon = True
        thread.start()

        logger.info('发送心跳')

        return

    def on_friend_talk_notice(self,ws, msg_dict):
        """
        处理好友聊天通知消息。

        参数:
        - ws: WebSocket连接对象，用于接收和发送消息。
        - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
        """
        msg = FriendTalkNoticeMessage()
        msg = ParseDict(msg_dict, msg)
        logger.info(f'FriendTalkNoticeMessage 收到的消息为: {msg}')

        if msg.WeChatId not in self.wx_info:
            logger.error('没有找到该微信，跳过')
            return

        wechat = self.wx_info[msg.WeChatId]
        logger.info(f'当前处理的微信为: {wechat}')

        workphone_msg = WorkPhoneMessage(msg,wechat)

        logger.debug("[wx_hook] wx_hook_msg message: {}".format(workphone_msg))

        context = self._compose_context(workphone_msg.ctype, workphone_msg.content, isgroup=workphone_msg.is_group,msg=workphone_msg)

        if context is None:
            logger.error("无法识别的消息类型，跳过")
            return

        # todo 黑白名单处理


        if context:
            # 增加需要的context
            context['wechat_account'] = wechat
            context['wxid'] = wechat['wechatid']

            # todo 后台做好后，从后台获取apikey的配置
            context['open_ai_api_base'] = "https://newapi.gkscrm.com/v1"
            context['open_ai_api_key'] = "sk-wwttAtdLcTfeF7F2Eb9d3592Bd4c487f8e8fA544D6C4BbA9"

            # 不需要添加at
            context['no_need_at'] = True

            logger.info("[WX] receiveMsg={}, context={}".format(workphone_msg, context))
            self.produce(context)



    def on_message(self, ws, message):
        logger.info("接受到的消息原文为 : %s" % message)

        received_data = json.loads(message)
        if 'msgType' not in received_data:
            return


        if received_data['msgType'] == 'DeviceAuthRsp':
            msg_dict = json.loads(received_data['message'])
            return self.on_device_auth(ws, msg_dict)

        if received_data['msgType'] == 'FriendTalkNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_friend_talk_notice(ws,msg_dict)

    def send(self, reply: Reply, context: Context):
        logger.info(f'[wx_hook] reply: {reply}')
        logger.info(f'[wx_hook] context: {context}')

        wx_account = context['wechat_account']
        receiver = context["receiver"]
        is_group = context["isgroup"]

        if reply.type == ReplyType.TEXT:

            send_msg = TalkToFriendTaskMessage(
                WeChatId=wx_account['wechatid'],
                FriendId=receiver,
                ContentType=EnumContentType.Text,
                Content=reply.content.encode('utf-8'),
            )
            if is_group:
                send_msg.Remark = context['session_id']

            logger.info(f'[wx_hook] 发送文本消息: {send_msg}')

            content = Any()
            content.Pack(send_msg)

            transport_message = TransportMessage(MsgType=EnumMsgType.TalkToFriendTask, Content=content)

            transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

            # 清理不必要的字段
            del transport_message_dict['Content']['@type']

            transport_message_json = json.dumps(transport_message_dict, indent=2)

            self.wsCli.send(transport_message_json)


