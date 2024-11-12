from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TakeLuckyMoneyTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "MsgSvrId", "MsgKey", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MSGKEY_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    MsgSvrId: int
    MsgKey: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., MsgKey: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
