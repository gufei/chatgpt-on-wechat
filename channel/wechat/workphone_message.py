import json

from app import redis_conn
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from lib.itchat.storage.messagequeue import logger
from workphone.FriendTalkNotice_pb2 import FriendTalkNoticeMessage
from workphone.TransportMessage_pb2 import EnumContentType


class WorkPhoneMessage(ChatMessage):
    def __init__(self, message:FriendTalkNoticeMessage,wechat:dict):
        super().__init__(message)

        self.msg_id = message.MsgId
        self.create_time = message.CreateTime
        if "@chatroom" in message.FriendId:
            self.is_group = True


        if message.ContentType == EnumContentType.Text:
            self.ctype = ContextType.TEXT
            self.content = message.Content.decode('utf-8')


        if self.is_group:
            group_json = redis_conn.hget("workphone_group_info_"+wechat['wechatid'], message.FriendId)
            group = json.loads(group_json)
            self.content = message.Content.decode('utf-8')
            lines = self.content.split(':',1)
            self.from_user_id = lines[0]
            self.to_user_id = message.FriendId
            self.to_user_nickname = group['nickname']
            self.other_user_id = message.FriendId
            self.other_user_nickname = group['nickname']
            self.content = lines[1].strip()

            self.actual_user_id = lines[0]
            # todo 实际发送者昵称，需要获取群成员信息后才能拿到
            self.actual_user_nickname = lines[0]
            self.self_display_name = wechat['wechatnick']

            self.is_at = False
            if message.Ext:
                at_list = message.Ext.split(',')
                if message.WeChatId in at_list:
                    self.is_at = True
            else:
                if "@" + wechat['wechatnick'] in self.content:
                    self.content = self.content.replace("@" + wechat['wechatnick'], "")
                    self.is_at = True

        else:
            self.from_user_id = message.FriendId
            self.from_user_nickname = message.NickName
            self.to_user_id = message.WeChatId
            self.to_user_nickname = wechat['wechatnick']
            self.other_user_id = message.FriendId
            self.other_user_nickname = message.NickName
            self.content = message.Content.decode('utf-8')





