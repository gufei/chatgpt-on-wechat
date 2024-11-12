from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class OneKeyLikeTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "TaskId", "Count", "EndType")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    ENDTYPE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    TaskId: int
    Count: int
    EndType: int
    def __init__(self, WeChatId: _Optional[str] = ..., TaskId: _Optional[int] = ..., Count: _Optional[int] = ..., EndType: _Optional[int] = ...) -> None: ...
