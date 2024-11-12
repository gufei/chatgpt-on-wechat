from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRoomDelNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "RoomId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    RoomId: str
    def __init__(self, WeChatId: _Optional[str] = ..., RoomId: _Optional[str] = ...) -> None: ...
