import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatRspMessage(_message.Message):
    __slots__ = ("WeChatId", "WeChatNo", "WeChatNick", "Avatar", "Country", "Province", "City", "Gender", "IsOnline", "IsLogined", "IsDelete", "LoginTime", "ModifyTime", "DeviceName", "LoginUnionId", "LoginAccountType", "IsUpgrading")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    WECHATNO_FIELD_NUMBER: _ClassVar[int]
    WECHATNICK_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    ISONLINE_FIELD_NUMBER: _ClassVar[int]
    ISLOGINED_FIELD_NUMBER: _ClassVar[int]
    ISDELETE_FIELD_NUMBER: _ClassVar[int]
    LOGINTIME_FIELD_NUMBER: _ClassVar[int]
    MODIFYTIME_FIELD_NUMBER: _ClassVar[int]
    DEVICENAME_FIELD_NUMBER: _ClassVar[int]
    LOGINUNIONID_FIELD_NUMBER: _ClassVar[int]
    LOGINACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    ISUPGRADING_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    WeChatNo: str
    WeChatNick: str
    Avatar: str
    Country: str
    Province: str
    City: str
    Gender: _TransportMessage_pb2.EnumGender
    IsOnline: bool
    IsLogined: bool
    IsDelete: bool
    LoginTime: int
    ModifyTime: int
    DeviceName: str
    LoginUnionId: int
    LoginAccountType: _TransportMessage_pb2.EnumAccountType
    IsUpgrading: bool
    def __init__(self, WeChatId: _Optional[str] = ..., WeChatNo: _Optional[str] = ..., WeChatNick: _Optional[str] = ..., Avatar: _Optional[str] = ..., Country: _Optional[str] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., IsOnline: bool = ..., IsLogined: bool = ..., IsDelete: bool = ..., LoginTime: _Optional[int] = ..., ModifyTime: _Optional[int] = ..., DeviceName: _Optional[str] = ..., LoginUnionId: _Optional[int] = ..., LoginAccountType: _Optional[_Union[_TransportMessage_pb2.EnumAccountType, str]] = ..., IsUpgrading: bool = ...) -> None: ...

class GetWeChatsRspMessage(_message.Message):
    __slots__ = ("UnionId", "AccountType", "SupplierId", "WeChats")
    UNIONID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    WECHATS_FIELD_NUMBER: _ClassVar[int]
    UnionId: int
    AccountType: _TransportMessage_pb2.EnumAccountType
    SupplierId: int
    WeChats: _containers.RepeatedCompositeFieldContainer[WeChatRspMessage]
    def __init__(self, UnionId: _Optional[int] = ..., AccountType: _Optional[_Union[_TransportMessage_pb2.EnumAccountType, str]] = ..., SupplierId: _Optional[int] = ..., WeChats: _Optional[_Iterable[_Union[WeChatRspMessage, _Mapping]]] = ...) -> None: ...
