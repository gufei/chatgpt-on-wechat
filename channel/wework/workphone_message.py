import json

from app import redis_conn
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from lib.itchat.storage.messagequeue import logger
from wecom.WFriendTalkNotice_pb2 import FriendTalkNoticeMessage
from wecom.WTransport_pb2 import EnumContentType


class WorkPhoneMessage(ChatMessage):
    def __init__(self, message:FriendTalkNoticeMessage,wechat:dict):
        super().__init__(message)

        self.msg_id = message.MsgId
        self.create_time = message.CreateTime
        # if "@chatroom" in message.ConvId:
        #     self.is_group = True
        self.is_group = False


        if message.ContentType == EnumContentType.Text:
            self.ctype = ContextType.TEXT
            self.content = message.Content.decode('utf-8')


        if self.is_group:
            group_json = redis_conn.hget("workphone_group_info_"+wechat['wechatid'], message.ConvId)
            if group_json:
                group = json.loads(group_json)
                self.to_user_nickname = group['nickname']
                self.other_user_nickname = group['nickname']

            self.content = message.Content.decode('utf-8')
            lines = self.content.split(':',1)
            self.from_user_id = lines[0]
            self.to_user_id = message.ConvId

            self.other_user_id = message.ConvId

            self.content = lines[1].strip()

            self.actual_user_id = lines[0]
            # todo 实际发送者昵称，需要获取群成员信息后才能拿到
            self.actual_user_nickname = lines[0]
            self.self_display_name = wechat['name']

            self.is_at = False
            if message.Ext:
                at_list = message.Ext.split(',')
                if message.WeChatId in at_list:
                    self.is_at = True
            else:
                if "@" + wechat['name'] in self.content:
                    self.content = self.content.replace("@" + wechat['name'], "")
                    self.is_at = True

        else:
            self.from_user_id = message.ConvId
            self.from_user_nickname = message.SenderName
            self.to_user_id = message.WxId
            self.to_user_nickname = wechat['name']
            self.other_user_id = message.ConvId
            self.other_user_nickname = message.SenderName
            self.content = message.Content.decode('utf-8')





