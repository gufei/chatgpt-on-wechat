from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FindContactTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Content")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Content: str
    def __init__(self, WeChatId: _Optional[str] = ..., Content: _Optional[str] = ...) -> None: ...
