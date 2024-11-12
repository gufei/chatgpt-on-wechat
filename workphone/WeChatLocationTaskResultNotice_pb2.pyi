from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatLocationTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "Success", "Lng", "Lat")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    LNG_FIELD_NUMBER: _ClassVar[int]
    LAT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    Success: bool
    Lng: float
    Lat: float
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., Success: bool = ..., Lng: _Optional[float] = ..., Lat: _Optional[float] = ...) -> None: ...
