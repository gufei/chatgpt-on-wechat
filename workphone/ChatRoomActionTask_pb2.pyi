from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumChatRoomAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    RoomName: _ClassVar[EnumChatRoomAction]
    ModifyPublicNoti: _ClassVar[EnumChatRoomAction]
    AddMember: _ClassVar[EnumChatRoomAction]
    KickMember: _ClassVar[EnumChatRoomAction]
    RoomShowName: _ClassVar[EnumChatRoomAction]
    AddToPhonebook: _ClassVar[EnumChatRoomAction]
    NewMsgNoti: _ClassVar[EnumChatRoomAction]
    ExitRoom: _ClassVar[EnumChatRoomAction]
    CreateRoom: _ClassVar[EnumChatRoomAction]
    ViewAllMember: _ClassVar[EnumChatRoomAction]
    TransferOwner: _ClassVar[EnumChatRoomAction]
    SetVerify: _ClassVar[EnumChatRoomAction]
    AddManager: _ClassVar[EnumChatRoomAction]
    DelManager: _ClassVar[EnumChatRoomAction]
    SetRemark: _ClassVar[EnumChatRoomAction]
    SetTop: _ClassVar[EnumChatRoomAction]
RoomName: EnumChatRoomAction
ModifyPublicNoti: EnumChatRoomAction
AddMember: EnumChatRoomAction
KickMember: EnumChatRoomAction
RoomShowName: EnumChatRoomAction
AddToPhonebook: EnumChatRoomAction
NewMsgNoti: EnumChatRoomAction
ExitRoom: EnumChatRoomAction
CreateRoom: EnumChatRoomAction
ViewAllMember: EnumChatRoomAction
TransferOwner: EnumChatRoomAction
SetVerify: EnumChatRoomAction
AddManager: EnumChatRoomAction
DelManager: EnumChatRoomAction
SetRemark: EnumChatRoomAction
SetTop: EnumChatRoomAction

class ChatRoomActionTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "ChatRoomId", "Action", "Content", "IntValue", "taskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATROOMID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INTVALUE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    ChatRoomId: str
    Action: EnumChatRoomAction
    Content: str
    IntValue: int
    taskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., ChatRoomId: _Optional[str] = ..., Action: _Optional[_Union[EnumChatRoomAction, str]] = ..., Content: _Optional[str] = ..., IntValue: _Optional[int] = ..., taskId: _Optional[int] = ...) -> None: ...
