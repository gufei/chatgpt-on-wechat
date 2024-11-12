from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PostFriendDetectTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "TaskId", "Message", "OnlyCheck", "SkipHour", "Mode", "Max")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    ONLYCHECK_FIELD_NUMBER: _ClassVar[int]
    SKIPHOUR_FIELD_NUMBER: _ClassVar[int]
    MODE_FIELD_NUMBER: _ClassVar[int]
    MAX_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    TaskId: int
    Message: str
    OnlyCheck: bool
    SkipHour: int
    Mode: int
    Max: int
    def __init__(self, WeChatId: _Optional[str] = ..., TaskId: _Optional[int] = ..., Message: _Optional[str] = ..., OnlyCheck: bool = ..., SkipHour: _Optional[int] = ..., Mode: _Optional[int] = ..., Max: _Optional[int] = ...) -> None: ...
