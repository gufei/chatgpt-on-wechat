import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatOnlineNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "WeChatNo", "WeChatNick", "Gender", "Country", "Province", "City", "Avatar", "IMEI", "Phone")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    WECHATNO_FIELD_NUMBER: _ClassVar[int]
    WECHATNICK_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    WeChatNo: str
    WeChatNick: str
    Gender: _TransportMessage_pb2.EnumGender
    Country: str
    Province: str
    City: str
    Avatar: str
    IMEI: str
    Phone: str
    def __init__(self, WeChatId: _Optional[str] = ..., WeChatNo: _Optional[str] = ..., WeChatNick: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Country: _Optional[str] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Avatar: _Optional[str] = ..., IMEI: _Optional[str] = ..., Phone: _Optional[str] = ...) -> None: ...
