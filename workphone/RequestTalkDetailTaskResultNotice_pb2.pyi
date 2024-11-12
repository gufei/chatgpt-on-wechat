from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestTalkDetailTaskResultNoticeMessage(_message.Message):
    __slots__ = ("MsgId", "WeChatId", "FriendId", "Content", "IsOriginal")
    MSGID_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ISORIGINAL_FIELD_NUMBER: _ClassVar[int]
    MsgId: int
    WeChatId: str
    FriendId: str
    Content: bytes
    IsOriginal: bool
    def __init__(self, MsgId: _Optional[int] = ..., WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Content: _Optional[bytes] = ..., IsOriginal: bool = ...) -> None: ...
