import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendReqMessage(_message.Message):
    __slots__ = ("FriendId", "FriendNo", "FriendNick", "Avatar", "Reason", "Gender", "Province", "City", "Source", "SourceUser", "ReqTime", "State", "FirstReq")
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    FRIENDNO_FIELD_NUMBER: _ClassVar[int]
    FRIENDNICK_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    REASON_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    SOURCE_FIELD_NUMBER: _ClassVar[int]
    SOURCEUSER_FIELD_NUMBER: _ClassVar[int]
    REQTIME_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    FIRSTREQ_FIELD_NUMBER: _ClassVar[int]
    FriendId: str
    FriendNo: str
    FriendNick: str
    Avatar: str
    Reason: str
    Gender: _TransportMessage_pb2.EnumGender
    Province: str
    City: str
    Source: int
    SourceUser: str
    ReqTime: int
    State: int
    FirstReq: int
    def __init__(self, FriendId: _Optional[str] = ..., FriendNo: _Optional[str] = ..., FriendNick: _Optional[str] = ..., Avatar: _Optional[str] = ..., Reason: _Optional[str] = ..., Gender: _Optional[_Union[_TransportMessage_pb2.EnumGender, str]] = ..., Province: _Optional[str] = ..., City: _Optional[str] = ..., Source: _Optional[int] = ..., SourceUser: _Optional[str] = ..., ReqTime: _Optional[int] = ..., State: _Optional[int] = ..., FirstReq: _Optional[int] = ...) -> None: ...

class FriendAddReqListNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Requests")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    REQUESTS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Requests: _containers.RepeatedCompositeFieldContainer[FriendReqMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., Requests: _Optional[_Iterable[_Union[FriendReqMessage, _Mapping]]] = ...) -> None: ...
