import json

from app import redis_conn
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from lib.itchat.storage.messagequeue import logger
from wecom.WFriendTalkNotice_pb2 import FriendTalkNoticeMessage
from wecom.WTransport_pb2 import EnumContentType


class WorkPhoneMessage(ChatMessage):
    def __init__(self, message:FriendTalkNoticeMessage,wechat:dict,voice_path:str):
        super().__init__(message)

        self.msg_id = message.MsgId
        self.create_time = message.CreateTime
        # if "@chatroom" in message.ConvId:
        #     self.is_group = True
        # logger.info("[WX]message {}".format(message))
        if message.ConvType == 1:
            self.is_group = True

        if message.ContentType == EnumContentType.Text:
            self.ctype = ContextType.TEXT
            self.content = message.Content.decode('utf-8')
        if message.ContentType == EnumContentType.QuoteMsg:
            self.ctype = ContextType.TEXT
            content = message.Content.decode('utf-8')
            if not content.startswith('{'):
                content = content.split(':', 1)[-1].strip()

            content_json = json.loads(content)
            self.content = content_json.get('text', "")
        elif message.ContentType == EnumContentType.Voice:
            self.ctype = ContextType.VOICE
            self.content = voice_path


        if self.is_group:
            self.to_user_nickname = message.SenderName
            self.other_user_nickname = message.SenderName

            self.content = message.Content.decode('utf-8')
            logger.info("[WX]self.content {}".format(self.content))
            self.from_user_id = message.SenderId
            self.to_user_id = message.ConvId

            self.other_user_id = message.ConvId
            self.actual_user_id = message.SenderId
            # todo 实际发送者昵称，需要获取群成员信息后才能拿到
            self.actual_user_nickname = message.SenderName
            self.self_display_name = wechat['name']
            logger.info("[WX]self.self_display_name {}".format(self.self_display_name))
            self.is_at = False
            # if message.Ext:
            #     at_list = message.Ext.split(',')
            #     if message.WeChatId in at_list:
            #         self.is_at = True
            # else:
            #
            if message.AtMe:
                self.content = self.content.replace("@" + wechat['name'], "")
                self.is_at = True

        else:
            self.from_user_id = message.ConvId
            self.from_user_nickname = message.SenderName
            self.to_user_id = message.WxId
            self.to_user_nickname = wechat['name']
            self.other_user_id = message.ConvId
            self.other_user_nickname = message.SenderName
            if message.ContentType == EnumContentType.Text:
                self.content = message.Content.decode('utf-8')
            elif message.ContentType == EnumContentType.Voice:
                self.content = voice_path





