from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostFriendDetectCountNoticeMessage(_message.Message):
    __slots__ = ("TaskId", "Count", "DelCount", "IsFinished", "SkipCount", "Zombies", "WeChatId")
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    DELCOUNT_FIELD_NUMBER: _ClassVar[int]
    ISFINISHED_FIELD_NUMBER: _ClassVar[int]
    SKIPCOUNT_FIELD_NUMBER: _ClassVar[int]
    ZOMBIES_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TaskId: int
    Count: int
    DelCount: int
    IsFinished: bool
    SkipCount: int
    Zombies: _containers.RepeatedScalarFieldContainer[str]
    WeChatId: str
    def __init__(self, TaskId: _Optional[int] = ..., Count: _Optional[int] = ..., DelCount: _Optional[int] = ..., IsFinished: bool = ..., SkipCount: _Optional[int] = ..., Zombies: _Optional[_Iterable[str]] = ..., WeChatId: _Optional[str] = ...) -> None: ...
