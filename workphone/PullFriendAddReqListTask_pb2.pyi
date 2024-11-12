from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullFriendAddReqListTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "StartTime", "OnlyNew", "GetAll")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ONLYNEW_FIELD_NUMBER: _ClassVar[int]
    GETALL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    StartTime: int
    OnlyNew: bool
    GetAll: bool
    def __init__(self, WeChatId: _Optional[str] = ..., StartTime: _Optional[int] = ..., OnlyNew: bool = ..., GetAll: bool = ...) -> None: ...
