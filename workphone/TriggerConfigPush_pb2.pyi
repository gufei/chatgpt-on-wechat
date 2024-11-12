from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerConfigPushMessage(_message.Message):
    __slots__ = ("IMEI", "WeChatId")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI: str
    WeChatId: str
    def __init__(self, IMEI: _Optional[str] = ..., WeChatId: _Optional[str] = ...) -> None: ...
