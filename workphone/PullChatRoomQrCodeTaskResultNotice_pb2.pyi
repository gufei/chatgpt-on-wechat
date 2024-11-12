from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullChatRoomQrCodeTaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "ChatRoomId", "QrCodeUrl", "TaskId", "WeChatId", "ErrMsg")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CHATROOMID_FIELD_NUMBER: _ClassVar[int]
    QRCODEURL_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    ChatRoomId: str
    QrCodeUrl: str
    TaskId: int
    WeChatId: str
    ErrMsg: str
    def __init__(self, Success: bool = ..., ChatRoomId: _Optional[str] = ..., QrCodeUrl: _Optional[str] = ..., TaskId: _Optional[int] = ..., WeChatId: _Optional[str] = ..., ErrMsg: _Optional[str] = ...) -> None: ...
