import base64
import json
import threading
import time

import traceback
import websocket
from google.protobuf.json_format import MessageToDict, ParseDict

from wecom.WDeviceAuthReq_pb2 import DeviceAuthReqMessage
from wecom.WFriendTalkNotice_pb2 import FriendTalkNoticeMessage
from wecom.WTransport_pb2 import TransportMessage, EnumMsgType, EnumContentType

from wecom.WDeviceAuthRsp_pb2 import DeviceAuthRspMessage


from google.protobuf.any_pb2 import Any

from common.log import logger


class WecomClient(threading.Thread):

    """
    This class is used to connect to the websocket server.
    """

    access_token = ""

    heart_beat_event = threading.Event()

    def __init__(self, url, credential):
        self.url = url
        self.credential = credential
        threading.Thread.__init__(self)
        self.daemon = True

    def run(self):
        # Running the run_forever() in a seperate thread.
        websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(self.url,
                                         on_message=self.on_message,
                                         on_error=self.on_error,
                                         on_close=self.on_close,
                                         on_open=self.on_open)

        self.ws.run_forever()

    def send(self, data):
        # Wait till websocket is connected.
        while not self.ws.sock.connected:
            time.sleep(0.25)

        logger.info(f'Sending data...{data}')
        self.ws.send(data)

    def send_heart_beat_event(self, interval, event, data):
        while not event.is_set():
            self.send(data)
            # 模拟发送请求
            time.sleep(interval)

    def stop(self):
        logger.info('Stopping the websocket...')
        self.heart_beat_event.set()
        self.ws.keep_running = False
        self.ws.close()

    def on_message(self, ws, message):
        logger.info(f'Received data...{message}')
        received_data = json.loads(message)
        if 'msgType' not in  received_data:
            return

        if received_data['msgType'] == 'DeviceAuthRsp':
            msg_dict = json.loads(received_data['message'])
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
                target=self.send_heart_beat_event, args=(30, self.heart_beat_event, json.dumps(heart_beat_req)))
            thread.daemon = True
            thread.start()


            logger.info('发送心跳')

            return

        if received_data['msgType'] == 'FriendTalkNotice':
            logger.info('收到消息')
            msg_dict = json.loads(received_data['message'])
            msg = FriendTalkNoticeMessage()
            msg = ParseDict(msg_dict, msg)
            logger.info(msg)

            if msg.WeChatId not in self.wx_info:
                logger.error('没有找到该微信，跳过')

            wechat = self.wx_info[msg.WeChatId]
            logger.info('微信信息')
            logger.info(wechat)


            # if "@chatroom" in msg.FriendId:
            #     logger.info('收到群消息')
            #     if msg.ContentType == EnumContentType.Text:
            #         logger.info('收到文本消息')
            #         content = msg.Content.decode('utf-8')
            #         lines = content.split(':\n')
            #         from_wxid = lines[0]
            #         content = lines[1]
            #         logger.info(from_wxid)
            #         logger.info(content)
            #
            #
            #         at = False
            #
            #         if msg.Ext:
            #             logger.info('at 账号列表')
            #             at_list = msg.Ext.split(',')
            #             logger.info(at_list)
            #             if msg.WeChatId in at_list:
            #                 at = True
            #         else:
            #             if "@"+wechat['wechatnick'] in content:
            #                 content = content.replace("@"+wechat['wechatnick'], "")
            #                 at = True
            #
            #
            #         if at:
            #             send_msg = TalkToFriendTaskMessage(
            #                 WeChatId=msg.WeChatId,
            #                 FriendId=msg.FriendId,
            #                 ContentType=EnumContentType.Text,
            #                 Content="这是一个群里的自动回复，并加上了at".encode('utf-8'),
            #                 Remark=from_wxid
            #             )
            #
            #             content = Any()
            #             content.Pack(send_msg)
            #
            #             transport_message = TransportMessage(MsgType=EnumMsgType.TalkToFriendTask, Content=content)
            #
            #             transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)
            #
            #             # 清理不必要的字段
            #             del transport_message_dict['Content']['@type']
            #
            #             transport_message_json = json.dumps(transport_message_dict, indent=2)
            #
            #             self.send(transport_message_json)
            #
            #
            # else:
            if msg.ContentType == EnumContentType.Text:
                logger.info('收到个人消息')
                content = msg.Content.decode('utf-8')
                logger.info(content)

    def on_error(self, ws, error):
        logger.info('Received error...')
        logger.error(error)
        logger.error(f"stack:{traceback.print_exc()}")

    def on_close(self, ws, close_status_code, close_msg):
        logger.info('Received close...')
        logger.info(close_status_code)
        logger.info(close_msg)
        logger.info('Closed the connection...')

        # 重新连接
        logger.info('重新连接...')
        self.run()

    def on_open(self, ws):
        logger.info('进行认证...')
        device_auth = DeviceAuthReqMessage(
            AuthType=DeviceAuthReqMessage.EnumAuthType.Username,
            Credential=base64.b64encode(self.credential.encode('utf-8')).decode('utf-8')
        )

        device_map = {
            "AuthType":2,
            "Credential":base64.b64encode(self.credential.encode('utf-8')).decode('utf-8')
        }

        device_auth = ParseDict(device_map, device_auth)

        content  = Any()
        content.Pack(device_auth)

        transport_message  = TransportMessage(MsgType=EnumMsgType.DeviceAuthReq, Content=content)

        transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

        transport_message_dict['Content'] = device_map

        transport_message_json = json.dumps(transport_message_dict, indent=2)

        self.send(transport_message_json)


