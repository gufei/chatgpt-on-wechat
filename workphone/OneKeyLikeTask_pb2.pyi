from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OneKeyLikeTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "TaskId", "Rate", "EndTime", "Num", "TimeOut")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    RATE_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    NUM_FIELD_NUMBER: _ClassVar[int]
    TIMEOUT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    TaskId: int
    Rate: int
    EndTime: int
    Num: int
    TimeOut: int
    def __init__(self, WeChatId: _Optional[str] = ..., TaskId: _Optional[int] = ..., Rate: _Optional[int] = ..., EndTime: _Optional[int] = ..., Num: _Optional[int] = ..., TimeOut: _Optional[int] = ...) -> None: ...
