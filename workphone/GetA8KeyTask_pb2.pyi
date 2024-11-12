from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetA8KeyTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Type", "Url", "UserName", "MsgSvrId", "Reason", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Type: int
    Url: str
    UserName: str
    MsgSvrId: str
    Reason: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Type: _Optional[int] = ..., Url: _Optional[str] = ..., UserName: _Optional[str] = ..., MsgSvrId: _Optional[str] = ..., Reason: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
