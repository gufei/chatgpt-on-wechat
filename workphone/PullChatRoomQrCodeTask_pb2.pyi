from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullChatRoomQrCodeTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "ChatRoomId", "taskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATROOMID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    ChatRoomId: str
    taskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., ChatRoomId: _Optional[str] = ..., taskId: _Optional[int] = ...) -> None: ...
