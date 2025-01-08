import json
from bridge.context import Context, ContextType

from telegram import Update
from channel.chat_message import ChatMessage

class TelegramMessage(ChatMessage):
    def __init__(self, update: Update, extra: dict):
        super().__init__(update.message.text)

        self.msg_id = update.message.message_id
        self.create_time = update.message.date.time()

        self.ctype = ContextType.TEXT
        self.content = update.message.text

        self.is_group = False
        self.from_user_id = update.message.from_user.id
        self.from_user_nickname = update.message.from_user.first_name
        self.to_user_id = extra.to_user_id
        self.to_user_nickname = extra.to_user_nickname
        self.other_user_id = update.message.from_user.id
        self.other_user_nickname = update.message.from_user.first_name
        self.content = update.message.text
