import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendMessage(_message.Message):
    __slots__ = ("FriendId", "FriendNo", "FriendNick", "Memo", "Gender", "Country", "Province", "City", "Avatar", "Remark", "Type", "LabelIds", "Phone", "Desc", "Source", "SourceExt")
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    FRIENDNO_FIELD_NUMBER: _ClassVar[int]
    FRIENDNICK_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    LABELIDS_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEEXT_FIELD_NUMBER: _ClassVar[int]
    FriendId: str
    FriendNo: str
    FriendNick: str
    Memo: str
    Gender: _TransportMessage_pb2.EnumGender
    Country: str
    Province: str
    City: str
    Avatar: str
    Remark: str
    Type: int
    LabelIds: str
    Phone: str
    Desc: str
    Source: int
    SourceExt: str
    def __init__(self, FriendId: _Optional[str] = ..., FriendNo: _Optional[str] = ..., FriendNick: _Optional[str] = ..., Memo: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Country: _Optional[str] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Avatar: _Optional[str] = ..., Remark: _Optional[str] = ..., Type: _Optional[int] = ..., LabelIds: _Optional[str] = ..., Phone: _Optional[str] = ..., Desc: _Optional[str] = ..., Source: _Optional[int] = ..., SourceExt: _Optional[str] = ...) -> None: ...

class FriendAddNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Friend")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Friend: FriendMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Friend: _Optional[_Union[FriendMessage, _Mapping]] = ...) -> None: ...
