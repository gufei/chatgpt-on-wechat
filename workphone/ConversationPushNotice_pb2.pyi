from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ConversMessage(_message.Message):
    __slots__ = ("UserName", "Digest", "DigestUser", "IsSend", "MsgCnt", "UnreadCnt", "UpdateTime", "IsTop", "IsSilent", "ShowName", "Avatar", "AtCount", "Remark", "IsUnusual")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    DIGESTUSER_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    MSGCNT_FIELD_NUMBER: _ClassVar[int]
    UNREADCNT_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    ISTOP_FIELD_NUMBER: _ClassVar[int]
    ISSILENT_FIELD_NUMBER: _ClassVar[int]
    SHOWNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ATCOUNT_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    ISUNUSUAL_FIELD_NUMBER: _ClassVar[int]
    UserName: str
    Digest: str
    DigestUser: str
    IsSend: bool
    MsgCnt: int
    UnreadCnt: int
    UpdateTime: int
    IsTop: bool
    IsSilent: bool
    ShowName: str
    Avatar: str
    AtCount: int
    Remark: str
    IsUnusual: bool
    def __init__(self, UserName: _Optional[str] = ..., Digest: _Optional[str] = ..., DigestUser: _Optional[str] = ..., IsSend: bool = ..., MsgCnt: _Optional[int] = ..., UnreadCnt: _Optional[int] = ..., UpdateTime: _Optional[int] = ..., IsTop: bool = ..., IsSilent: bool = ..., ShowName: _Optional[str] = ..., Avatar: _Optional[str] = ..., AtCount: _Optional[int] = ..., Remark: _Optional[str] = ..., IsUnusual: bool = ...) -> None: ...

class ConversationPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Convers", "Size", "Count", "Page", "TaskId", "Offset", "NextOffset")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONVERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    NEXTOFFSET_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Convers: _containers.RepeatedCompositeFieldContainer[ConversMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    Offset: int
    NextOffset: int
    def __init__(self, WeChatId: _Optional[str] = ..., Convers: _Optional[_Iterable[_Union[ConversMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ..., Offset: _Optional[int] = ..., NextOffset: _Optional[int] = ...) -> None: ...
