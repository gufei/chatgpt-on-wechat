from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryHbStatusTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "HbUrl")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    HBURL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    HbUrl: str
    def __init__(self, WeChatId: _Optional[str] = ..., HbUrl: _Optional[str] = ...) -> None: ...
