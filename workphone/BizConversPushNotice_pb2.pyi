from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BizConversMessage(_message.Message):
    __slots__ = ("UserName", "Digest", "DigestUser", "IsSend", "MsgCnt", "UnreadCnt", "UpdateTime", "ShowName", "Avatar")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    DIGEST_FIELD_NUMBER: _ClassVar[int]
    DIGESTUSER_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    MSGCNT_FIELD_NUMBER: _ClassVar[int]
    UNREADCNT_FIELD_NUMBER: _ClassVar[int]
    UPDATETIME_FIELD_NUMBER: _ClassVar[int]
    SHOWNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    UserName: str
    Digest: str
    DigestUser: str
    IsSend: bool
    MsgCnt: int
    UnreadCnt: int
    UpdateTime: int
    ShowName: str
    Avatar: str
    def __init__(self, UserName: _Optional[str] = ..., Digest: _Optional[str] = ..., DigestUser: _Optional[str] = ..., IsSend: bool = ..., MsgCnt: _Optional[int] = ..., UnreadCnt: _Optional[int] = ..., UpdateTime: _Optional[int] = ..., ShowName: _Optional[str] = ..., Avatar: _Optional[str] = ...) -> None: ...

class BizConversPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Convers", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONVERS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Convers: _containers.RepeatedCompositeFieldContainer[BizConversMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Convers: _Optional[_Iterable[_Union[BizConversMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
