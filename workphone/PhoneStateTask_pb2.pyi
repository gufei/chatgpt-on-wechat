from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneStateTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Imei")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Imei: str
    def __init__(self, WeChatId: _Optional[str] = ..., Imei: _Optional[str] = ...) -> None: ...
