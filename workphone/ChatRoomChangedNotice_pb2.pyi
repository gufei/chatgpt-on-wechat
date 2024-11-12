from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumChatRoomChange(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Change_MemberList: _ClassVar[EnumChatRoomChange]
    Change_PublicNotice: _ClassVar[EnumChatRoomChange]
    Change_NickName: _ClassVar[EnumChatRoomChange]
    Change_ShowName: _ClassVar[EnumChatRoomChange]
    Change_MyShowName: _ClassVar[EnumChatRoomChange]
    Change_Owner: _ClassVar[EnumChatRoomChange]
    Change_Avatar: _ClassVar[EnumChatRoomChange]
    Change_MemberAdd: _ClassVar[EnumChatRoomChange]
    Change_MemberDel: _ClassVar[EnumChatRoomChange]
Change_MemberList: EnumChatRoomChange
Change_PublicNotice: EnumChatRoomChange
Change_NickName: EnumChatRoomChange
Change_ShowName: EnumChatRoomChange
Change_MyShowName: EnumChatRoomChange
Change_Owner: EnumChatRoomChange
Change_Avatar: EnumChatRoomChange
Change_MemberAdd: EnumChatRoomChange
Change_MemberDel: EnumChatRoomChange

class ChatRoomChangedNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "UserName", "What", "Content")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    WHAT_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    UserName: str
    What: EnumChatRoomChange
    Content: str
    def __init__(self, WeChatId: _Optional[str] = ..., UserName: _Optional[str] = ..., What: _Optional[_Union[EnumChatRoomChange, str]] = ..., Content: _Optional[str] = ...) -> None: ...
