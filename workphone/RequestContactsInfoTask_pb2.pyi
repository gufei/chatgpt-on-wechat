from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestContactsInfoTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Contact", "Local")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    LOCAL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Contact: str
    Local: bool
    def __init__(self, WeChatId: _Optional[str] = ..., Contact: _Optional[str] = ..., Local: bool = ...) -> None: ...
