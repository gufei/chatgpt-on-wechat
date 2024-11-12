import FriendAddNotice_pb2 as _FriendAddNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Friends", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Friends: _containers.RepeatedCompositeFieldContainer[_FriendAddNotice_pb2.FriendMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Friends: _Optional[_Iterable[_Union[_FriendAddNotice_pb2.FriendMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
