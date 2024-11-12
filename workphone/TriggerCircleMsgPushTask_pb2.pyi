from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerCircleMsgPushTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "OnlyComment", "GetAll", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    ONLYCOMMENT_FIELD_NUMBER: _ClassVar[int]
    GETALL_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    OnlyComment: bool
    GetAll: bool
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., OnlyComment: bool = ..., GetAll: bool = ..., TaskId: _Optional[int] = ...) -> None: ...
