from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatLoginNoticeRespMessage(_message.Message):
    __slots__ = ("WeChats",)
    WECHATS_FIELD_NUMBER: _ClassVar[int]
    WeChats: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, WeChats: _Optional[_Iterable[str]] = ...) -> None: ...
