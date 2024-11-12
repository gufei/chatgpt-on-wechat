from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QwUserMessage(_message.Message):
    __slots__ = ("UserId", "Name", "Avatar")
    USERID_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    UserId: str
    Name: str
    Avatar: str
    def __init__(self, UserId: _Optional[str] = ..., Name: _Optional[str] = ..., Avatar: _Optional[str] = ...) -> None: ...

class QwUserPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Users", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    USERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Users: _containers.RepeatedCompositeFieldContainer[QwUserMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Users: _Optional[_Iterable[_Union[QwUserMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
