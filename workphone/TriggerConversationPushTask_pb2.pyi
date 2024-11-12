from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerConversationPushTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "StartTime", "EndTime", "WithName", "TaskId", "Limit", "Offset")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    WITHNAME_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    LIMIT_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    StartTime: int
    EndTime: int
    WithName: bool
    TaskId: int
    Limit: int
    Offset: int
    def __init__(self, WeChatId: _Optional[str] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ..., WithName: bool = ..., TaskId: _Optional[int] = ..., Limit: _Optional[int] = ..., Offset: _Optional[int] = ...) -> None: ...
