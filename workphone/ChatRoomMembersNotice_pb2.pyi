import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class StrangerMessage(_message.Message):
    __slots__ = ("Wxid", "Alias", "Nickname", "Avatar", "Type", "Gender", "Country", "Province", "City", "Memo", "Signature")
    WXID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    SIGNATURE_FIELD_NUMBER: _ClassVar[int]
    Wxid: str
    Alias: str
    Nickname: str
    Avatar: str
    Type: int
    Gender: _TransportMessage_pb2.EnumGender
    Country: str
    Province: str
    City: str
    Memo: str
    Signature: str
    def __init__(self, Wxid: _Optional[str] = ..., Alias: _Optional[str] = ..., Nickname: _Optional[str] = ..., Avatar: _Optional[str] = ..., Type: _Optional[int] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Country: _Optional[str] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Memo: _Optional[str] = ..., Signature: _Optional[str] = ...) -> None: ...

class ChatRoomMembersNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Members")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MEMBERS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Members: _containers.RepeatedCompositeFieldContainer[StrangerMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., Members: _Optional[_Iterable[_Union[StrangerMessage, _Mapping]]] = ...) -> None: ...
