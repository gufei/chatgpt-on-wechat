import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FindContactTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "SearchText", "Success", "IsFriend", "UserName", "Alias", "NickName", "Gender", "Country", "Province", "City", "Avatar", "ErrMsg")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SEARCHTEXT_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ISFRIEND_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    SearchText: str
    Success: bool
    IsFriend: bool
    UserName: str
    Alias: str
    NickName: str
    Gender: _TransportMessage_pb2.EnumGender
    Country: str
    Province: str
    City: str
    Avatar: str
    ErrMsg: str
    def __init__(self, WeChatId: _Optional[str] = ..., SearchText: _Optional[str] = ..., Success: bool = ..., IsFriend: bool = ..., UserName: _Optional[str] = ..., Alias: _Optional[str] = ..., NickName: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Country: _Optional[str] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Avatar: _Optional[str] = ..., ErrMsg: _Optional[str] = ...) -> None: ...
