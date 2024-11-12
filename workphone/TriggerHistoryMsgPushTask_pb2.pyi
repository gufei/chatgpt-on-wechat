from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerHistoryMsgPushTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "StartTime", "EndTime", "Flag", "Count", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    StartTime: int
    EndTime: int
    Flag: int
    Count: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ..., Flag: _Optional[int] = ..., Count: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
