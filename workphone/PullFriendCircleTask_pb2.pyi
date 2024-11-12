from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullFriendCircleTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "StartTime", "Count", "RefTime", "RefSnsId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    REFTIME_FIELD_NUMBER: _ClassVar[int]
    REFSNSID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    StartTime: int
    Count: int
    RefTime: int
    RefSnsId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., StartTime: _Optional[int] = ..., Count: _Optional[int] = ..., RefTime: _Optional[int] = ..., RefSnsId: _Optional[int] = ...) -> None: ...
