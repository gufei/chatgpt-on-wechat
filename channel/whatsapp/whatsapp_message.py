import binascii
from tempfile import TemporaryFile, NamedTemporaryFile

import openai
import pilk

from bridge.context import ContextType
from channel.chat_message import ChatMessage
from common.log import logger
from config import conf
from xml.etree import ElementTree as ET


class WaHookMessage(ChatMessage):
    def __init__(self, data, channel):
        super().__init__(data)
        self.msg_id = data.get("MessageId")
        self.create_time = data.get("Timestamp")

        self.is_group = False

        self.ctype = ContextType.TEXT
        self.content = data.get("Message")

        self.from_user_id = data.get("From")
        self.from_user_nickname = data.get("DisplayName")
        self.to_user_id = data.get("To")
        self.to_user_nickname = data.get("Name")

        self.actual_user_id = self.from_user_id
        self.actual_user_nickname = self.from_user_nickname

        self.other_user_id = self.to_user_id
        self.other_user_nickname = self.to_user_nickname

        self.is_at = False

