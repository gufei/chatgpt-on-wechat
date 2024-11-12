from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRoomMessage(_message.Message):
    __slots__ = ("UserName", "NickName", "MemberList", "Owner", "Notice", "ShowNameList", "SelfDisplayName", "Avatar", "Verify", "MsgSilent", "Remark", "Type", "IsUnusual")
    class DisplayNameMessage(_message.Message):
        __slots__ = ("UserName", "ShowName", "Inviter", "Flag")
        USERNAME_FIELD_NUMBER: _ClassVar[int]
        SHOWNAME_FIELD_NUMBER: _ClassVar[int]
        INVITER_FIELD_NUMBER: _ClassVar[int]
        FLAG_FIELD_NUMBER: _ClassVar[int]
        UserName: str
        ShowName: str
        Inviter: str
        Flag: int
        def __init__(self, UserName: _Optional[str] = ..., ShowName: _Optional[str] = ..., Inviter: _Optional[str] = ..., Flag: _Optional[int] = ...) -> None: ...
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    MEMBERLIST_FIELD_NUMBER: _ClassVar[int]
    OWNER_FIELD_NUMBER: _ClassVar[int]
    NOTICE_FIELD_NUMBER: _ClassVar[int]
    SHOWNAMELIST_FIELD_NUMBER: _ClassVar[int]
    SELFDISPLAYNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    VERIFY_FIELD_NUMBER: _ClassVar[int]
    MSGSILENT_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    ISUNUSUAL_FIELD_NUMBER: _ClassVar[int]
    UserName: str
    NickName: str
    MemberList: _containers.RepeatedScalarFieldContainer[str]
    Owner: str
    Notice: str
    ShowNameList: _containers.RepeatedCompositeFieldContainer[ChatRoomMessage.DisplayNameMessage]
    SelfDisplayName: str
    Avatar: str
    Verify: int
    MsgSilent: bool
    Remark: str
    Type: int
    IsUnusual: bool
    def __init__(self, UserName: _Optional[str] = ..., NickName: _Optional[str] = ..., MemberList: _Optional[_Iterable[str]] = ..., Owner: _Optional[str] = ..., Notice: _Optional[str] = ..., ShowNameList: _Optional[_Iterable[_Union[ChatRoomMessage.DisplayNameMessage, _Mapping]]] = ..., SelfDisplayName: _Optional[str] = ..., Avatar: _Optional[str] = ..., Verify: _Optional[int] = ..., MsgSilent: bool = ..., Remark: _Optional[str] = ..., Type: _Optional[int] = ..., IsUnusual: bool = ...) -> None: ...

class ChatRoomPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "ChatRooms", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATROOMS_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    ChatRooms: _containers.RepeatedCompositeFieldContainer[ChatRoomMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., ChatRooms: _Optional[_Iterable[_Union[ChatRoomMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
