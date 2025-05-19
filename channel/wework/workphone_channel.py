import json
import random
import threading
import os
import time
from datetime import datetime
import requests
from google.protobuf.json_format import ParseDict, MessageToDict

from app import redis_conn, db_storage
from bridge.context import Context, ContextType
from bridge.reply import Reply, ReplyType
from bot.chatgpt.chat_gpt_session import ChatGPTSession
from bot.session_manager import SessionManager
from config import conf, load_config
from channel.chat_channel import ChatChannel
from channel.wework.workphone_message import WorkPhoneMessage
from common.expired_dict import ExpiredDict
from common.log import logger
from common.singleton import singleton
from lib.allow_block import check_allow_or_block_list
from lib.file_tool import is_image_file
from lib.wecom_client import WecomClient
from wecom.WDeviceAuthRsp_pb2 import DeviceAuthRspMessage
from wecom.WFriendTalkNotice_pb2 import FriendTalkNoticeMessage
from wecom.WTalkToFriendTask_pb2 import TalkToFriendTaskMessage
from wecom.WTransport_pb2 import TalkToFriendNotice
from wecom.WTransport_pb2 import EnumContentType, TransportMessage, EnumMsgType, EnumAccountType
from wecom.WGetWeChatsReq_pb2 import GetWeChatsReqMessage
from wecom.WTriggerCustomerPushTask_pb2 import TriggerCustomerPushTaskMessage
from wecom.WTriggerConversationPushTask_pb2 import TriggerConversationPushTaskMessage
import xml.etree.ElementTree as ET
from urllib.parse import urlparse
from google.protobuf.any_pb2 import Any


@singleton
class WorkPhoneChannel(ChatChannel):

    wx_info = dict()

    def __init__(self):
        super().__init__()
        self.receivedMsgs = ExpiredDict(60 * 60)
        self.session = SessionManager(ChatGPTSession, model=conf().get("model") or "gpt-4o")

    def on_get_wechats(self, wechats):
        for wx_info in wechats:
            logger.info(f"[on_get_chats]wx_info:{wx_info}")
            if wx_info is None:
                continue
            print(f"wx_info['wxid']: {wx_info['wxid']}")
            wxinfo = db_storage.get_info_by_wxid(wx_info['wxid'])
            print(f"wxinfo2: {wxinfo}")
            if wxinfo:
                # 更新
                organization_id = wxinfo["organization_id"]
                db_storage.update_wx_record(wx_info.get('wxid', ""), wx_info.get('deviceid', ""), "11", "", wx_info.get('name', ""), wx_info.get('phone', ""), wx_info.get('avatar', ""))
            else:
                print(f"创建")
                # 创建
                print(f"wx_info.get('deviceid', ''): {wx_info.get('deviceid', '')}")
                organization_id = 1
                db_storage.create_wx_record(wx_info.get('deviceid', ''), "11", wx_info.get('wxid', ""), "", wx_info.get('name', ""), wx_info.get('phone', ""), wx_info.get('avatar', ""), 3)
            wx_info["organization_id"] = organization_id
            self.wx_info[wx_info['wxid']] = wx_info
            print(f"wx_info: {wx_info}")
            self.get_customer_push_notice(wx_info['wxid'])
            self.get_conversation_push_notice(wx_info['wxid'])

            # 获取联系人


        logger.info(f"初始化账号数据完成")

    def on_get_customer_push_notice(self, wechats):
        if not wechats:
            return None
        wx_wxid = wechats.get("WxId")
        wx_wxinfo = db_storage.get_info_by_wxid(wx_wxid)
        if not wx_wxid or not wx_wxinfo:
            return None
        for wx_info in wechats.get("Contacts"):

            # if not self.wx_info.get(wx_wxid):
            #     return None

            organization_id = wx_wxinfo.get("organization_id", 0)
            labelIds = ", ".join(wx_info.get('LabelIds', []))
            wxinfo = db_storage.get_contact_by_wxid(wx_info['RemoteId'], wx_wxid)
            if wxinfo:
                print(f"更新")
                # 更新
                db_storage.update_contact_record(wx_wxid, wx_info.get('RemoteId', ""), "", wx_info.get('Name', ""), wx_info.get('Alias', ""), wx_info.get('Avatar', ""), labelIds, "", "", organization_id, wx_info.get('Mobile', ""))
            else:
                print(f"创建")
                # 创建
                db_storage.create_contact_record(wx_wxid, 1, wx_info.get('RemoteId', ""), "", wx_info.get('Name', ""), wx_info.get('Alias', ""), wx_info.get('Avatar', ""), labelIds, "", "", organization_id, 3, wx_info.get('Mobile', ""))

    def on_get_conversation_push_notice(self, wechats):
        if not wechats:
            return None
        wx_wxid = wechats.get("WxId")
        wx_wxinfo = db_storage.get_info_by_wxid(wx_wxid)
        if not wx_wxid or not wx_wxinfo:
            return None
        for Conver_info in wechats.get("Convers"):
            if Conver_info.get('RemoteId', "") == wx_wxid:
                continue
            if Conver_info.get('Type', 0) != 1:
                continue

            # if not self.wx_info.get(wx_wxid):
            #     return None

            organization_id = wx_wxinfo.get("organization_id", 0)
            # labelIds = ", ".join(Conver_info.get('LabelIds', []))
            wxinfo = db_storage.get_contact_by_wxid(Conver_info['RemoteId'], wx_wxid)
            if wxinfo:
                print(f"更新")
                # 更新
                db_storage.update_contact_record(wx_wxid, Conver_info.get('RemoteId', ""), "", Conver_info.get('Name', ""), Conver_info.get('Alias', ""), Conver_info.get('Avatar', ""), "", "", "", organization_id, Conver_info.get('Mobile', ""))
            else:
                print(f"创建")
                # 创建
                db_storage.create_contact_record(wx_wxid, 2, Conver_info.get('RemoteId', ""), "", Conver_info.get('Name', ""), Conver_info.get('Alias', ""), Conver_info.get('Avatar', ""), "", "", "", organization_id, 3, Conver_info.get('Mobile', ""))


    def startup(self):
        # 测试 credential: bwkf:rQRwCSOmplX3TtLJ
        self.wsCli = WecomClient("ws://wecom.gkscrm.com:15088", "")
        self.wsCli.start()
        self.wsCli.ws.on_message = self.on_message
        # self.get_wx_info()

    def on_device_auth(self, ws, msg_dict):
        """
        认证注册回调
        """
        msg = DeviceAuthRspMessage()
        msg = ParseDict(msg_dict, msg)
        self.access_token = msg.AccessToken
        self.union_id = msg.Extra.UnionId
        logger.info(f'认证完成 AccessToken:{self.access_token}')

        # 构造发送心跳包
        heart_beat_req = {
            "Id": 1001,
            "MsgType": "HeartBeatReq",
            "AccessToken": self.access_token,
            "Content": {}
        }

        thread = threading.Thread(
            target=self.wsCli.send_heart_beat_event, args=(30, self.wsCli.heart_beat_event, json.dumps(heart_beat_req)))
        thread.daemon = True
        thread.start()

        logger.info('发送心跳')
        self.get_wechats_resp()
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
        # if str(msg.WxId) not in self.wx_info:
        #     logger.error('没有找到该微信，跳过')
        #     return

        # 获取wxinfo账号信息
        wxinfo = db_storage.get_info_by_wxid(str(msg.WxId))
        if wxinfo is None:
            logger.error('没有找到该微信，跳过')
            return

        logger.info(f'当前处理的微信为: {wxinfo}')

        voice_path = ''
        if msg.ContentType == EnumContentType.Voice:
            # msg.ConvType == 1 代表是群聊
            if msg.ConvType == 1:
                # 语音群聊暂时不处理
                logger.error("企微-群语音消息暂时不处理")
                return

            voice_path = self.download_voice(msg.Content)
            if voice_path == '':
                logger.error("音频文件过长，不处理")
                return

            # 以下内容是本地开发语音识别功能时的适配代码
            # 需要从线上把语音文件（amr或mp3）文件挪到本地对应目录里
            # voice_info = "{\"duration\":2,\"size\":4118,\"thumbSize\":0,\"url\":\"http://chat.gkscrm.com:14086/juliao/20250321/F01A0EDF3CE06A9D927F8236043266FD.mp3\"}"
            # voice_path = self.download_voice(voice_info)

        workphone_msg = WorkPhoneMessage(msg, wxinfo, voice_path)

        logger.debug("[wx_hook] wx_hook_msg message: {}".format(workphone_msg))

        context = self._compose_context(workphone_msg.ctype, workphone_msg.content, isgroup=workphone_msg.is_group,msg=workphone_msg)

        if context is None:
            logger.error("无法识别的消息类型，跳过")
            return

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

        if workphone_msg.is_group and workphone_msg.is_at:
            context['session_id'] = msg.SenderId

        # 记录聊天内容
        session_id = "chatId-{}".format(str(msg.WxId) + "_" + str(msg.SenderId))
        session = self.session.session_reply(str(msg.Content.decode('utf-8')), session_id)
        logger.warn(f"question:{msg.Content} session.messages:{session.messages}")
        logger.info("[FriendTalkNotice] session.messages={}".format(session.messages))

        if context:
            # 增加需要的context
            # print(f"wechat: {wechat}")
            print(f"wechat['wechatid']: {wxinfo['wxid']}")
            print(f"wxinfo['organization_id']: {wxinfo['organization_id']}")
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
                agent_info = db_storage.get_agent_info(msg.WxId, "workphone_wecom")
                model = agent_info.get("model")
                if model is None or model == "":
                    model = "gpt-4o-mini"
                api_base = agent_info.get("api_base")
                if api_base is None or api_base == "":
                    api_base = "http://new-api.gkscrm.com/v1"
                api_key = agent_info.get("api_key")
                if api_key is None or api_key == "":
                    api_key = "sk-ZQRNypQOC8ID5WbpCdF263C58dF44271842e86D408Bb3848"
                context['open_ai_api_base'] = api_base
                context['open_ai_api_key'] = api_key
                context['open_ai_model'] = model
                # if agent_info and agent_info.get("type") == 2:
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
    def download_voice(self, voice_info):
        # 解析 URL
        voice_info = json.loads(voice_info)
        logger.info(f"voice_info: {voice_info}")
        url = voice_info['url']

        # 确定保存图片的目录
        directory = os.path.join(os.getcwd(), "tmp")
        # 如果目录不存在，则创建目录
        if not os.path.exists(directory):
            os.makedirs(directory)

        # # 如果音频文件过长 直接不处理
        # if int(voice_info['duration']) > 60:
        #     return ''

        parsed_url = urlparse(url)

        # 获取路径部分，并提取文件名
        file_name_with_ext = os.path.basename(parsed_url.path)
        file_name = os.path.splitext(file_name_with_ext)[0]
        if isinstance(file_name, bytes):
            file_name = file_name.decode("utf-8")

        # 把amr文件重命名为silk文件
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

    def on_talk_to_friend_notice(self, msg_dict):
        """
        处理好友聊天通知消息。

        参数:
        - ws: WebSocket连接对象，用于接收和发送消息。
        - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
        """
        msg = FriendTalkNoticeMessage()
        msg = ParseDict(msg_dict, msg)
        logger.info(f'[TalkToFriendNotice] 收到的消息为: {msg}')

        # 记录聊天内容
        session_id = "chatId-{}".format(str(msg.WxId) + "_" + str(msg.SenderId))
        session = self.session.session_reply(str(msg.Content.decode('utf-8')), session_id)
        logger.warn(f"question:{msg.Content} session.messages:{session.messages}")
        logger.info("[TalkToFriendNotice] session.messages={}".format(session.messages))
        return


    def on_message(self, ws, message):
        logger.info("接受到的消息原文为 : %s" % message)

        received_data = json.loads(message)
        if 'msgType' not in received_data:
            return

        if received_data['msgType'] == 'FriendTalkNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_friend_talk_notice(ws,msg_dict)

        if received_data['msgType'] == 'GetWeChatsResp':
            msg_dict = json.loads(received_data['message'])
            return self.on_get_wechats(msg_dict)

        if received_data['msgType'] == 'CustomerPushNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_get_customer_push_notice(msg_dict)

        if received_data['msgType'] == 'ConversationPushNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_get_conversation_push_notice(msg_dict)

        if received_data['msgType'] == 'DeviceAuthRsp':
            msg_dict = json.loads(received_data['message'])
            return self.on_device_auth(ws, msg_dict)

        # if received_data['msgType'] == 'ChatRoomAddNotice':
        #     msg_dict = json.loads(received_data['message'])
        #     return self.on_chat_room_add_notice(msg_dict)

        if received_data['msgType'] == 'TalkToFriendNotice':
            msg_dict = json.loads(received_data['message'])
            return self.on_talk_to_friend_notice(msg_dict)

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
                if content.lower().endswith(('.mp4', '.mov')):
                    content_type = EnumContentType.Video
                else:
                    content_type = EnumContentType.File
        msg_id = int(f"{int(time.time() * 1000)}{random.randint(1000, 9999)}")
        db_storage.set_msg_id_friend_id(msg_id, receiver)
        send_msg = TalkToFriendTaskMessage(
            WxId=int(wx_account['wxid']),
            ConvId=receiver,
            ContentType=content_type,
            Content=content.encode('utf-8'),
            TaskId=msg_id
        )

        if is_group and reply.type == ReplyType.TEXT:
            send_msg.AtSomeOne.append(context['session_id'])

        logger.info(f'[wx_hook] 发送文本消息: {send_msg}')

        content = Any()
        content.Pack(send_msg)

        transport_message = TransportMessage(MsgType=EnumMsgType.TalkToFriendTask, Content=content)

        transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

        # 清理不必要的字段
        del transport_message_dict['Content']['@type']

        transport_message_json = json.dumps(transport_message_dict, indent=2)

        self.wsCli.send(transport_message_json)

    def get_wechats_resp(self):
        send_msg = GetWeChatsReqMessage(
            id=str(0),
            AccountType=EnumAccountType.SubUser,
        )

        content = Any()
        content.Pack(send_msg)

        transport_message = TransportMessage(MsgType=EnumMsgType.GetWeChatsReq, Content=content)

        transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

        # 清理不必要的字段
        del transport_message_dict['Content']['@type']

        transport_message_json = json.dumps(transport_message_dict, indent=2)
        logger.info(f'[wx_hook] 获取微信列表: {send_msg}')
        self.wsCli.send(transport_message_json)

    def get_customer_push_notice(self, wx_id):
        send_msg = TriggerCustomerPushTaskMessage(
            WxId=wx_id,
        )

        content = Any()
        content.Pack(send_msg)

        transport_message = TransportMessage(MsgType=EnumMsgType.TriggerCustomerPushTask, Content=content)

        transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

        # 清理不必要的字段
        del transport_message_dict['Content']['@type']

        transport_message_json = json.dumps(transport_message_dict, indent=2)
        print(f"transport_message_json: {transport_message_json}")
        self.wsCli.send(transport_message_json)

    def get_conversation_push_notice(self, wx_id):
        send_msg = TriggerConversationPushTaskMessage(
            WxId=wx_id,
        )

        content = Any()
        content.Pack(send_msg)

        transport_message = TransportMessage(MsgType=EnumMsgType.TriggerConversationPushTask, Content=content)

        transport_message_dict = MessageToDict(transport_message, preserving_proto_field_name=True)

        # 清理不必要的字段
        del transport_message_dict['Content']['@type']

        transport_message_json = json.dumps(transport_message_dict, indent=2)
        print(f"transport_message_json: {transport_message_json}")
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

    # def on_chat_room_members_notice(self, msg_dict):
    #     """
    #     处理聊天消息同步。
    #
    #     参数:
    #     - ws: WebSocket连接对象，用于接收和发送消息。
    #     - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
    #     """
    #     msg = ChatRoomMembersNoticeMessage()
    #     msg = ParseDict(msg_dict, msg)
    #     logger.info(f'ChatRoomMembersNotice 收到的消息为: {msg}')
    #
    #     if msg_dict["WeChatId"] not in self.wx_info:
    #         logger.error('没有找到该微信，跳过')
    #         return
    #
    #     members_tuples = [(msg.WeChatId, member.Wxid, member.SenderName, member.Avatar) for member in
    #                       msg.Members]
    #     db_storage.add_wp_chatroom_member(msg.WeChatId, members_tuples)

    # def on_chatroom_push_notice(self, msg_dict):
    #     """
    #     处理聊天消息同步。
    #
    #     参数:
    #     - ws: WebSocket连接对象，用于接收和发送消息。
    #     - msg_dict: 字典类型的原始消息，包含好友聊天通知的所有信息。
    #     """
    #     # msg = ChatRoomMembersNoticeMessage()
    #     # msg = ParseDict(msg_dict, msg)
    #     logger.info(f'ChatroomPushNotice 收到的消息为: {msg_dict}')
    #
    #     if msg_dict["WeChatId"] not in self.wx_info:
    #         logger.error('没有找到该微信，跳过')
    #         return
    #
    #     members_tuples = [(msg_dict["WeChatId"], chat_room["UserName"], chat_room["NickName"], chat_room["Owner"], chat_room["Avatar"], json.dumps(chat_room["MemberList"]), json.dumps(chat_room["ShowNameList"])) for chat_room in
    #                       msg_dict["ChatRooms"]]
    #     db_storage.add_wp_chatroom(msg_dict["WeChatId"], members_tuples)
