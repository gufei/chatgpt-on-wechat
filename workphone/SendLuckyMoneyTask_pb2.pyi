from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendLuckyMoneyTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "Money", "Number", "Passwd", "Wish", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MONEY_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    PASSWD_FIELD_NUMBER: _ClassVar[int]
    WISH_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    Money: int
    Number: int
    Passwd: str
    Wish: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Money: _Optional[int] = ..., Number: _Optional[int] = ..., Passwd: _Optional[str] = ..., Wish: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
