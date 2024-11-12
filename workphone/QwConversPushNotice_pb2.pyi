from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class QwConversMessage(_message.Message):
    __slots__ = ("UserName", "Digest", "IsSend", "MsgCnt", "UnreadCnt", "UpdateTime", "IsTop", "IsSilent", "ShowName", "Avatar", "AtCount", "Parent", "ParentName", "Owner", "UserList", "RoomFlag")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    MSGCNT_FIELD_NUMBER: _ClassVar[int]
    UNREADCNT_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    ISTOP_FIELD_NUMBER: _ClassVar[int]
    ISSILENT_FIELD_NUMBER: _ClassVar[int]
    SHOWNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ATCOUNT_FIELD_NUMBER: _ClassVar[int]
    PARENT_FIELD_NUMBER: _ClassVar[int]
    PARENTNAME_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    USERLIST_FIELD_NUMBER: _ClassVar[int]
    ROOMFLAG_FIELD_NUMBER: _ClassVar[int]
    UserName: str
    Digest: str
    IsSend: bool
    MsgCnt: int
    UnreadCnt: int
    UpdateTime: int
    IsTop: bool
    IsSilent: bool
    ShowName: str
    Avatar: str
    AtCount: int
    Parent: str
    ParentName: str
    Owner: str
    UserList: str
    RoomFlag: int
    def __init__(self, UserName: _Optional[str] = ..., Digest: _Optional[str] = ..., IsSend: bool = ..., MsgCnt: _Optional[int] = ..., UnreadCnt: _Optional[int] = ..., UpdateTime: _Optional[int] = ..., IsTop: bool = ..., IsSilent: bool = ..., ShowName: _Optional[str] = ..., Avatar: _Optional[str] = ..., AtCount: _Optional[int] = ..., Parent: _Optional[str] = ..., ParentName: _Optional[str] = ..., Owner: _Optional[str] = ..., UserList: _Optional[str] = ..., RoomFlag: _Optional[int] = ...) -> None: ...

class QwConversPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Convers", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONVERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Convers: _containers.RepeatedCompositeFieldContainer[QwConversMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Convers: _Optional[_Iterable[_Union[QwConversMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
