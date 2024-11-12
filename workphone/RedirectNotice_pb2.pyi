from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RedirectNoticeMessage(_message.Message):
    __slots__ = ("Type", "ServerUrl", "ServerPort", "UploadUrl")
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SERVERURL_FIELD_NUMBER: _ClassVar[int]
    SERVERPORT_FIELD_NUMBER: _ClassVar[int]
    UPLOADURL_FIELD_NUMBER: _ClassVar[int]
    Type: int
    ServerUrl: str
    ServerPort: int
    UploadUrl: str
    def __init__(self, Type: _Optional[int] = ..., ServerUrl: _Optional[str] = ..., ServerPort: _Optional[int] = ..., UploadUrl: _Optional[str] = ...) -> None: ...
