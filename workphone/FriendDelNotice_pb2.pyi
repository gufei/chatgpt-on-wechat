from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FriendDelNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "Reason")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    Reason: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Reason: _Optional[int] = ...) -> None: ...
