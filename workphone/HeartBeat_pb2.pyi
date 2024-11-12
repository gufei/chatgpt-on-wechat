from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class HeartBeatMessage(_message.Message):
    __slots__ = ("Imei", "WeChatId")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    Imei: str
    WeChatId: str
    def __init__(self, Imei: _Optional[str] = ..., WeChatId: _Optional[str] = ...) -> None: ...
