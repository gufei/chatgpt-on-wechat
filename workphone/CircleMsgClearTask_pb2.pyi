from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CircleMsgClearTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "CommentId", "IsRead")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    ISREAD_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    CommentId: int
    IsRead: bool
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., CommentId: _Optional[int] = ..., IsRead: bool = ...) -> None: ...
