from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendMultiPictureTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "Pics", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    PICS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    Pics: _containers.RepeatedScalarFieldContainer[str]
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Pics: _Optional[_Iterable[str]] = ..., TaskId: _Optional[int] = ...) -> None: ...
