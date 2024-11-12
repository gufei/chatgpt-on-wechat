from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenShotTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Type", "Param", "Param2", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    PARAM_FIELD_NUMBER: _ClassVar[int]
    PARAM2_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Type: int
    Param: str
    Param2: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Type: _Optional[int] = ..., Param: _Optional[str] = ..., Param2: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
