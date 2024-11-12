from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PhoneStateWarningNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Imei", "BatteryLevel", "ChargingState", "NetType", "SdcardFree", "SdcardTotal")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    BATTERYLEVEL_FIELD_NUMBER: _ClassVar[int]
    CHARGINGSTATE_FIELD_NUMBER: _ClassVar[int]
    NETTYPE_FIELD_NUMBER: _ClassVar[int]
    SDCARDFREE_FIELD_NUMBER: _ClassVar[int]
    SDCARDTOTAL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Imei: str
    BatteryLevel: int
    ChargingState: int
    NetType: str
    SdcardFree: int
    SdcardTotal: int
    def __init__(self, WeChatId: _Optional[str] = ..., Imei: _Optional[str] = ..., BatteryLevel: _Optional[int] = ..., ChargingState: _Optional[int] = ..., NetType: _Optional[str] = ..., SdcardFree: _Optional[int] = ..., SdcardTotal: _Optional[int] = ...) -> None: ...
