import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendAddReqeustNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "FriendNo", "FriendNick", "Reason", "Avatar", "Source", "SourceUser", "Gender", "Province", "City")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    FRIENDNO_FIELD_NUMBER: _ClassVar[int]
    FRIENDNICK_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEUSER_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    FriendNo: str
    FriendNick: str
    Reason: str
    Avatar: str
    Source: int
    SourceUser: str
    Gender: _TransportMessage_pb2.EnumGender
    Province: str
    City: str
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., FriendNo: _Optional[str] = ..., FriendNick: _Optional[str] = ..., Reason: _Optional[str] = ..., Avatar: _Optional[str] = ..., Source: _Optional[int] = ..., SourceUser: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ...) -> None: ...
