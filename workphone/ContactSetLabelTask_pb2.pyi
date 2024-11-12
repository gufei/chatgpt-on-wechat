from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContactSetLabelTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "LabelIds", "taskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    LABELIDS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    LabelIds: _containers.RepeatedScalarFieldContainer[int]
    taskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., LabelIds: _Optional[_Iterable[int]] = ..., taskId: _Optional[int] = ...) -> None: ...
