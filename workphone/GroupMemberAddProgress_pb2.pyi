from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GroupMemberAddTaskDetailMessage(_message.Message):
    __slots__ = ("wxId", "alias", "nickname", "avatar", "gender", "country", "province", "city", "updateTime", "status")
    WXID_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    GENDER_FIELD_NUMBER: _ClassVar[int]
    COUNTRY_FIELD_NUMBER: _ClassVar[int]
    PROVINCE_FIELD_NUMBER: _ClassVar[int]
    CITY_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    wxId: str
    alias: str
    nickname: str
    avatar: str
    gender: int
    country: str
    province: str
    city: str
    updateTime: int
    status: int
    def __init__(self, wxId: _Optional[str] = ..., alias: _Optional[str] = ..., nickname: _Optional[str] = ..., avatar: _Optional[str] = ..., gender: _Optional[int] = ..., country: _Optional[str] = ..., province: _Optional[str] = ..., city: _Optional[str] = ..., updateTime: _Optional[int] = ..., status: _Optional[int] = ...) -> None: ...

class GroupMemberAddProgressMessage(_message.Message):
    __slots__ = ("status", "suspendType", "progress", "totalQuantity", "waitSendQuantity", "sendingQuantity", "sendedQuantity", "passedQuantity", "ignoredQuantity", "detailList")
    STATUS_FIELD_NUMBER: _ClassVar[int]
    SUSPENDTYPE_FIELD_NUMBER: _ClassVar[int]
    PROGRESS_FIELD_NUMBER: _ClassVar[int]
    TOTALQUANTITY_FIELD_NUMBER: _ClassVar[int]
    WAITSENDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SENDINGQUANTITY_FIELD_NUMBER: _ClassVar[int]
    SENDEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    PASSEDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    IGNOREDQUANTITY_FIELD_NUMBER: _ClassVar[int]
    DETAILLIST_FIELD_NUMBER: _ClassVar[int]
    status: int
    suspendType: int
    progress: float
    totalQuantity: int
    waitSendQuantity: int
    sendingQuantity: int
    sendedQuantity: int
    passedQuantity: int
    ignoredQuantity: int
    detailList: _containers.RepeatedCompositeFieldContainer[GroupMemberAddTaskDetailMessage]
    def __init__(self, status: _Optional[int] = ..., suspendType: _Optional[int] = ..., progress: _Optional[float] = ..., totalQuantity: _Optional[int] = ..., waitSendQuantity: _Optional[int] = ..., sendingQuantity: _Optional[int] = ..., sendedQuantity: _Optional[int] = ..., passedQuantity: _Optional[int] = ..., ignoredQuantity: _Optional[int] = ..., detailList: _Optional[_Iterable[_Union[GroupMemberAddTaskDetailMessage, _Mapping]]] = ...) -> None: ...
