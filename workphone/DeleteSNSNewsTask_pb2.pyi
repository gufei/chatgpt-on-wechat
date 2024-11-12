from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class DeleteSNSNewsTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
