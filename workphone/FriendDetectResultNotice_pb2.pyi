from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FriendDetectResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "TaskId", "StartTime", "EndTime", "IsFinished", "Count", "SkipCount", "DelCount", "Zombies", "BlockedList", "BannedList", "CanceledList")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    ISFINISHED_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    SKIPCOUNT_FIELD_NUMBER: _ClassVar[int]
    DELCOUNT_FIELD_NUMBER: _ClassVar[int]
    ZOMBIES_FIELD_NUMBER: _ClassVar[int]
    BLOCKEDLIST_FIELD_NUMBER: _ClassVar[int]
    BANNEDLIST_FIELD_NUMBER: _ClassVar[int]
    CANCELEDLIST_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    TaskId: int
    StartTime: int
    EndTime: int
    IsFinished: bool
    Count: int
    SkipCount: int
    DelCount: int
    Zombies: _containers.RepeatedScalarFieldContainer[str]
    BlockedList: _containers.RepeatedScalarFieldContainer[str]
    BannedList: _containers.RepeatedScalarFieldContainer[str]
    CanceledList: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, WeChatId: _Optional[str] = ..., TaskId: _Optional[int] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ..., IsFinished: bool = ..., Count: _Optional[int] = ..., SkipCount: _Optional[int] = ..., DelCount: _Optional[int] = ..., Zombies: _Optional[_Iterable[str]] = ..., BlockedList: _Optional[_Iterable[str]] = ..., BannedList: _Optional[_Iterable[str]] = ..., CanceledList: _Optional[_Iterable[str]] = ...) -> None: ...
