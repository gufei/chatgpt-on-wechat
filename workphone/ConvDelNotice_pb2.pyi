from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ConvDelNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "ConvName", "Avatar")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONVNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    ConvName: str
    Avatar: str
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., ConvName: _Optional[str] = ..., Avatar: _Optional[str] = ...) -> None: ...
