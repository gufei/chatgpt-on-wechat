from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RemittanceTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "Money", "Passwd", "Memo", "TaskId", "RoomId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    PASSWD_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    ROOMID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    Money: int
    Passwd: str
    Memo: str
    TaskId: int
    RoomId: str
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Money: _Optional[int] = ..., Passwd: _Optional[str] = ..., Memo: _Optional[str] = ..., TaskId: _Optional[int] = ..., RoomId: _Optional[str] = ...) -> None: ...
