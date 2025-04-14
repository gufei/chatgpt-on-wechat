import json
from app import redis_conn, db_storage

from app import redis_conn
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from lib.itchat.storage.messagequeue import logger
from workphone.FriendTalkNotice_pb2 import FriendTalkNoticeMessage
from workphone.TransportMessage_pb2 import EnumContentType


class WorkPhoneMessage(ChatMessage):
    def __init__(self, message:FriendTalkNoticeMessage,wechat:dict, voice_path:str):
        super().__init__(message)

        self.msg_id = message.MsgId
        self.create_time = message.CreateTime
        if "@chatroom" in message.FriendId:
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
            self.content = content_json.get('title', "")
        elif message.ContentType == EnumContentType.Voice:
            self.ctype = ContextType.VOICE
            self.content = voice_path


        if self.is_group:
            hkey = "workphone_group_info_"+wechat['wxid']
            group_json = redis_conn.hget(hkey, message.FriendId)
            if group_json:
                group = json.loads(group_json)
                self.to_user_nickname = group['nickname']
                self.other_user_nickname = group['nickname']
            else:
                group = db_storage.get_contact_by_wxwxid_wxid(wechat['wxid'], message.FriendId)
                logger.info(f"group info is:{group} wx_wxid:{wechat['wxid']} wxid:{message.FriendId}")
                self.to_user_nickname = group['nickname']
                self.other_user_nickname = group['nickname']
                redis_conn.hset(hkey, message.FriendId, json.dumps(group))

            self.content = message.Content.decode('utf-8')
            lines = self.content.split(':',1)
            self.from_user_id = lines[0]
            self.to_user_id = message.FriendId

            self.other_user_id = message.FriendId

            self.content = lines[1].strip()

            self.actual_user_id = lines[0]
            # todo 实际发送者昵称，需要获取群成员信息后才能拿到
            self.actual_user_nickname = lines[0]
            self.self_display_name = wechat['nickname']

            self.is_at = False
            if message.Ext:
                at_list = message.Ext.split(',')
                if message.WeChatId in at_list:
                    self.is_at = True
            else:
                if "@" + wechat['nickname'] in self.content:
                    self.content = self.content.replace("@" + wechat['nickname'], "")
                    self.is_at = True

        else:
            self.from_user_id = message.FriendId
            self.from_user_nickname = message.NickName
            self.to_user_id = message.WeChatId
            self.to_user_nickname = wechat['nickname']
            self.other_user_id = message.FriendId
            self.other_user_nickname = message.NickName
            if message.ContentType == EnumContentType.Voice:
                self.content = voice_path
            else:
                self.content = message.Content.decode('utf-8')





