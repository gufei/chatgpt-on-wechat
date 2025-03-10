
from bridge.context import ContextType
from channel.chat_message import ChatMessage
from common.log import logger


class WeworkHookMessage(ChatMessage):
    def __init__(self, msg, channel, isgroup, isat):
        super().__init__(msg)

        selfwxid = msg.get('sender_id')
        # logger.debug(f"[wework_hook] msg is {msg}")


        self.msg_id = msg.get("msg_id")
        self.create_time = msg.get("msg_time")

        self.is_group = isgroup
        self.is_at = isat
        self.receiver = msg.get("receiver_id")

        # self.ctype = ContextType.TEXT
        # self.content = msg.get("msg_content")
        if msg.get("msg_type") == 1:
            self.ctype = ContextType.TEXT
            self.content = msg.get("msg_content")
        elif msg.get("msg_type") in [2,3]:
            self.ctype = ContextType.IMAGE
            self.content = msg.get("msg_content")
        elif msg.get("msg_type") == 4:
            self.ctype = ContextType.VIDEO
            self.content = msg.get("msg_content")
        else:
            raise NotImplementedError("Unsupported message type: {}".format(msg.get("msgtype")))

        if self.is_group:
            self.from_user_id = msg.get("sender_id")
            self.from_user_nickname = ''
            self.to_user_id = msg.get("receiver_id")
            self.to_user_nickname = channel.getNickName(msg.get("robot_id"), msg.get('receiver_id'))
        else:
            self.from_user_id = msg.get("sender_id")
            self.from_user_nickname = ''
            self.to_user_id = msg.get("receiver_id")
            self.to_user_nickname = ''

        self.actual_user_id = msg.get('sender_id')


        # logger.debug(f"[wework_hook] actual_user_nickname is {self.from_user_nickname}")
        self.actual_user_nickname = self.from_user_nickname

        if self.is_group:
            if "fromgid" in msg:
                group = channel.getGroup(msg.get("fromgid"))
                self.other_user_id = msg.get("fromgid")
                self.other_user_nickname = group.get("gname")
                self.group_id = msg.get("fromgid")
                self.group_name = group.get("gname")
            else:
                group = channel.getGroup(msg.get("fromid"))
                self.other_user_id = msg.get("fromid")
                self.other_user_nickname = group.get("gname")
                self.group_id = msg.get("fromid")
                self.group_name = group.get("gname")
        else:
            if self.from_user_id != selfwxid:
                self.other_user_id = self.from_user_id
                self.other_user_nickname = self.from_user_nickname
            else:
                self.other_user_id = self.to_user_id
                self.other_user_nickname = self.to_user_nickname
