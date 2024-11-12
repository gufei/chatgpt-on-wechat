from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullCallLogTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "StartTime", "EndTime", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    StartTime: int
    EndTime: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
