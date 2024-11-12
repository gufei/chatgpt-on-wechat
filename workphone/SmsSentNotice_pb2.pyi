from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SmsSentNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "SmsId", "Type")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    SMSID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    SmsId: int
    Type: int
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., SmsId: _Optional[int] = ..., Type: _Optional[int] = ...) -> None: ...
