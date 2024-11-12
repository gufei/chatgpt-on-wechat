from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatOfflineNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "Reason")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    Reason: int
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., Reason: _Optional[int] = ...) -> None: ...
