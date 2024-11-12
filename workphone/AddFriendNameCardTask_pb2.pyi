from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddFriendNameCardTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "MsgSvrId", "Message", "Remark", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    MsgSvrId: int
    Message: str
    Remark: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., Message: _Optional[str] = ..., Remark: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
