import base64
import json
import threading
import os
import time
from datetime import datetime

import requests
from google.protobuf.json_format import ParseDict, MessageToDict

from app import redis_conn, db_storage
from bridge.context import Context, ContextType
from bridge.reply import Reply, ReplyType
from channel.chat_channel import ChatChannel
from channel.wechat.workphone_message import WorkPhoneMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from common.singleton import singleton
from lib.allow_block import check_allow_or_block_list
from lib.file_tool import is_image_file
from lib.itchat.components.messages import send_msg
from lib.wsclient import WebSocketClient
from workphone.ChatRoomAddNotice_pb2 import ChatRoomAddNoticeMessage
from workphone.ChatRoomMembersNotice_pb2 import ChatRoomMembersNoticeMessage
from workphone.DeviceAuthRsp_pb2 import DeviceAuthRspMessage
from workphone.FriendTalkNotice_pb2 import FriendTalkNoticeMessage
from workphone.TalkToFriendTask_pb2 import TalkToFriendTaskMessage
from workphone.TransportMessage_pb2 import EnumContentType, TransportMessage, EnumMsgType
import xml.etree.ElementTree as ET
from urllib.parse import urlparse, parse_qs
from google.protobuf.any_pb2 import Any


@singleton
class WorkPhoneChannel(ChatChannel):

    wx_info = dict()

    def __init__(self):
        super().__init__()
        self.receivedMsgs = ExpiredDict(60 * 60)
        # self.get_wx_info()

    def get_wx_info(self):
        logger.info(f"初始化账号数据")
        url = "http://chat.gkscrm.com:13086/pc/GetWeChatsReq?id=11"
        response = requests.request("POST", url)

        if response.status_code != 200:
            logger.error("Error while fetching the wechats")

        res = response.json()

        if res.get('code') != 0:
            logger.error('Error while fetching the wechats')

        for wx_info in res['data']:
            wechatid = wx_info.get("wechatid")
            if wechatid:
                self.wx_info[wechatid] = wx_info

                redis_conn.hset('workphone_wechat_info', wechatid, json.dumps(wx_info))

                url = "http://chat.gkscrm.com:13086/pc/GetWechatFriendList?cid=" + str(wx_info['cid']) + "&wechatid=" + wx_info[
                    'wechatid']
                response = requests.request("POST", url)
                if response.status_code != 200:
                    logger.error("Error while fetching the friends")
                    continue
                res = response.json()
                for friend in res['data']:
                    if friend['type'] == 0:
                        redis_conn.hset('workphone_contact_info_' + wechatid, friend['friendid'],
                                        json.dumps(friend))
                    elif friend['type'] == 1:
                        redis_conn.hset('workphone_group_info_' + wechatid, friend['friendid'],
                                        json.dumps(friend))

                wx = redis_conn.hget('workphone_wechat_info',wechatid)

        logger.info(f"初始化账号数据完成")



    def startup(self):
        # 测试 credential: bwkf:rQRwCSOmplX3TtLJ
        self.wsCli = WebSocketClient("ws://chat.gkscrm.com:13088", "bwkf:rQRwCSOmplX3TtLJ")
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

        # if msg.WeChatId not in self.wx_info:
        #     logger.error('没有找到该微信，跳过')
        #     return
        # wechat = self.wx_info[msg.WeChatId]

        # 获取wxinfo账号信息
        wxinfo = db_storage.get_info_by_wxid(msg.WeChatId)
        if wxinfo is None:
            logger.error('没有找到该微信，跳过')
            return

        logger.info(f'当前处理的微信为: {wxinfo}')

        # 语音文件已经在本地了 /data/work-phone/filesjuliao/20250320/xxxx.amr 或者 mp3
        # 这里只要把 arm 或 mp3 转成 wav 即可，后续openai 可根据wav文件识别成文字
        voice_path = ''
        if msg.ContentType == EnumContentType.Voice:
            content = str(msg.Content)

            if "chatroom" in msg.FriendId:
                logger.error('个微-群语音消息暂时不处理')
                return

            # 正常语音文件：http://chat.gkscrm.com:14086/juliao/20250320/1224CA2AE1976C14A5D93503BB7B0D1C.mp3?duration=2880
            # 群语音文件：wxid_k7p37xnoig8y21:http://chat.gkscrm.com:14086/juliao/20250328/6C17CC337D83B347713054941384ADEB.mp3?duration=2140
            # 如果发现是群语音文件，暂时不处理

            voice_path = self.download_voice(msg.Content)

            # 以下内容是本地开发语音识别功能时的适配代码
            # 需要从线上把语音文件（amr或mp3）文件挪到本地对应目录里
            # voice_url = 'http://chat.gkscrm.com:14086/juliao/20250320/1224CA2AE1976C14A5D93503BB7B0D1C.mp3?duration=2880'
            # voice_path = self.download_voice(voice_url)

        workphone_msg = WorkPhoneMessage(msg,wxinfo,voice_path)

        logger.debug("[wx_hook] wx_hook_msg message: {}".format(workphone_msg))

        context = self._compose_context(workphone_msg.ctype, workphone_msg.content, isgroup=workphone_msg.is_group,msg=workphone_msg)

        if context is None:
            logger.error("无法识别的消息类型，跳过")
            return

        logger.debug(f"[wx_hook] 获取到的账号信息: wxinfo: {wxinfo}")

        if not wxinfo:
            logger.error("没有找到该账号，跳过")
            return

        if wxinfo['server_id'] > 0:
            logger.error("不是工作手机的账号")
            return

        # 黑白名单处理
        if check_allow_or_block_list(context, wxinfo) is False:
            logger.debug(f"[wx_hook] check_allow_or_block_list failed")
            return self


        if context:
            # 增加需要的context
            context['wechat_account'] = wxinfo
            context['wxid'] = wxinfo['wxid']
            context['organization_id'] = wxinfo['organization_id']

            if wxinfo['agent_id'] == 0:
                if wxinfo['api_base'] != '':
                    context['open_ai_api_base'] = wxinfo['api_base']
                    context['open_ai_api_key'] = wxinfo['api_key']
                else:
                    context['open_ai_api_base'] = "http://new-api.gkscrm.com/v1"
                    context['open_ai_api_key'] = "sk-wwttAtdLcTfeF7F2Eb9d3592Bd4c487f8e8fA544D6C4BbA9"
            else:
                agent_info = db_storage.get_agent_info(msg.WeChatId, "workphone")
                model = agent_info.get("model")
                if model is None or model == "":
                    model = "gpt-4o-mini"
                api_base = agent_info.get("api_base")
                if api_base is None or api_base == "":
                    api_base = "http://new-api.gkscrm.com/v1"
                api_base += "/chat/completions"
                api_key = agent_info.get("api_key")
                if api_key is None or api_key == "":
                    api_key = "sk-ZQRNypQOC8ID5WbpCdF263C58dF44271842e86D408Bb3848"
                context['open_ai_api_base'] = api_base
                context['open_ai_api_key'] = api_key
                context['open_ai_model'] = model
                # if agent_info and agent_info.get("type") == 2:
                #
                #     context['open_ai_api_base'] = agent_info.get("api_base", "http://new-api.gkscrm.com/v1") + "/chat/completions"
                #     context['open_ai_api_key'] = agent_info.get("api_key", "sk-ZQRNypQOC8ID5WbpCdF263C58dF44271842e86D408Bb3848")
                #     context['open_ai_model'] = agent_info.get("model")
                # else:
                #     context['open_ai_api_base'] = "http://new-api.gkscrm.com/v1"
                #     context['open_ai_api_key'] = "sk-wwttAtdLcTfeF7F2Eb9d3592Bd4c487f8e8fA544D6C4BbA9"

            # 不需要添加at
            context['no_need_at'] = True

            logger.info("[WX] receiveMsg={}, context={}".format(workphone_msg, context))
            self.produce(context)

    # 获取文件路径
    def download_voice(self, url):
        # 确定保存的目录
        directory = os.path.join(os.getcwd(), "tmp")
        # 如果目录不存在，则创建目录
        if not os.path.exists(directory):
            os.makedirs(directory)

        # 解析 URL
        parsed_url = urlparse(url)

        # 获取路径部分，并提取文件名
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name = os.path.splitext(file_name_with_ext)[0]
        if isinstance(file_name, bytes):
            file_name = file_name.decode("utf-8")

        # #检查语音时长
        # parsed_params = parse_qs(parsed_url.query)
        # duration = parsed_params['duration'][0]
        # seconds = int(duration)/1000
        # if seconds > 60:
        #     return ''

        # 下载视频
        date = datetime.now().strftime("%Y%m%d")
        amr_url = f"http://chat.gkscrm.com:14086/juliao/{date}/{file_name}.amr"
        silk_path = os.path.join(directory, f"{file_name}.silk")
        wav_path = os.path.join(directory, f"{file_name}.wav")

        try:
            response = requests.get(amr_url)
            with open(silk_path, "wb") as f:
                f.write(response.content)

        except Exception as e:
            print("保存文件失败：")
            print(e)
            return ''

        # 把silk文件转wav文件
        from voice.audio_convert import any_to_wav
        any_to_wav(silk_path, wav_path)

        return wav_path


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

        # if received_data['msgType'] == 'ChatRoomAddNotice':
        #     msg_dict = json.loads(received_data['message'])
        #     return self.on_chat_room_add_notice(msg_dict)

        if received_data['msgType'] == 'ChatRoomMembersNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_chat_room_members_notice(msg_dict)

        if received_data['msgType'] == 'ChatroomPushNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_chatroom_push_notice(msg_dict)

    def send(self, reply: Reply, context: Context):
        logger.info(f'[wx_hook] reply: {reply}')
        logger.info(f'[wx_hook] context: {context}')
        wx_account = context['wechat_account']

        if reply.receiver:
            receiver = reply.receiver
        else:
            receiver = context["receiver"]
        is_group = context["isgroup"]

        if reply.type == ReplyType.TEXT:
            content_type = EnumContentType.Text
            content = reply.content
        elif reply.type == ReplyType.ShiPinHao:
            content_type = EnumContentType.ShiPinHao

            # 解码为字节串
            decoded_bytes = base64.b64decode(reply.content)
            # 解码为字符串
            content = decoded_bytes.decode('utf-8')
        elif reply.type == ReplyType.LOCATION:
            content_type = EnumContentType.Location
            if reply.content.startswith('<?xml version'):
                root = ET.fromstring(reply.content)
                location_element = root.find('location')
                if location_element is None:
                    logger.error("定位格式错误，XML 中没有找到 <location> 元素")
                    return
                location_info = {
                    "LocationX": location_element.get('x'),
                    "LocationY": location_element.get('y'),
                    "Label": location_element.get('label'),
                    "Title": location_element.get('poiname')
                }
                content = json.dumps(location_info,ensure_ascii=False)
            else:
                content = reply.content
        else:
            content = reply.content
            if is_image_file(content):
                content_type = EnumContentType.Picture
            else:
                if content.lower().endswith(('.mp4', '.mov', '.avi', '.wmv', '.mpg', '.mpeg')):
                    content_type = EnumContentType.Video
                else:
                    content_type = EnumContentType.File


        send_msg = TalkToFriendTaskMessage(
            WeChatId=wx_account['wxid'],
            FriendId=receiver,
            ContentType=content_type,
            Content=content.encode('utf-8')
        )

        if is_group and reply.type == ReplyType.TEXT:
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

    # def on_chat_room_add_notice(self, msg_dict):
    #     """
    #     处理聊天消息同步。
    #
    #     参数:
    #     - ws: WebSocket连接对象，用于接收和发送消息。
    #     - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
    #     """
    #     # msg = ChatRoomAddNoticeMessage()
    #     # msg = ParseDict(msg_dict, msg)
    #     logger.info(f'ChatRoomAddNotice 收到的消息为: {msg_dict}')
    #
    #     if msg_dict["WeChatId"] not in self.wx_info:
    #         logger.error('没有找到该微信，跳过')
    #         return
    #
    #     db_storage.add_wp_chatroom(msg_dict["WeChatId"], msg_dict["ChatRoom"]["UserName"], msg_dict["ChatRoom"]["NickName"], msg_dict["ChatRoom"]["Owner"], msg_dict["ChatRoom"]["Avatar"], msg_dict["ChatRoom"]["MemberList"], msg_dict["ChatRoom"]["ShowNameList"])

    def on_chat_room_members_notice(self, msg_dict):
        """
        处理聊天消息同步。

        参数:
        - ws: WebSocket连接对象，用于接收和发送消息。
        - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
        """
        msg = ChatRoomMembersNoticeMessage()
        msg = ParseDict(msg_dict, msg)
        logger.info(f'ChatRoomMembersNotice 收到的消息为: {msg}')

        # if msg_dict["WeChatId"] not in self.wx_info:
        #     logger.error('没有找到该微信，跳过')
        #     return
        wxinfo = db_storage.get_info_by_wxid(msg_dict["WeChatId"])
        if wxinfo is None:
            logger.error('没有找到该微信，跳过')
            return

        members_tuples = [(msg.WeChatId, member.Wxid, member.Nickname, member.Avatar) for member in
                          msg.Members]
        db_storage.add_wp_chatroom_member(msg.WeChatId, members_tuples)

    def on_chatroom_push_notice(self, msg_dict):
        """
        处理聊天消息同步。

        参数:
        - ws: WebSocket连接对象，用于接收和发送消息。
        - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
        """
        # msg = ChatRoomMembersNoticeMessage()
        # msg = ParseDict(msg_dict, msg)
        logger.info(f'ChatroomPushNotice 收到的消息为: {msg_dict}')

        # if msg_dict["WeChatId"] not in self.wx_info:
        #     logger.error('没有找到该微信，跳过')
        #     return
        wxinfo = db_storage.get_info_by_wxid(msg_dict["WeChatId"])
        if wxinfo is None:
            logger.error('没有找到该微信，跳过')
            return

        members_tuples = [(msg_dict["WeChatId"], chat_room["UserName"], chat_room["NickName"], chat_room["Owner"], chat_room["Avatar"], json.dumps(chat_room["MemberList"]), json.dumps(chat_room["ShowNameList"])) for chat_room in
                          msg_dict["ChatRooms"]]
        db_storage.add_wp_chatroom(msg_dict["WeChatId"], members_tuples)
