from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddFriendInChatRoomTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "ChatroomId", "FriendId", "Message", "Remark", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATROOMID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    ChatroomId: str
    FriendId: str
    Message: str
    Remark: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., ChatroomId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Message: _Optional[str] = ..., Remark: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
