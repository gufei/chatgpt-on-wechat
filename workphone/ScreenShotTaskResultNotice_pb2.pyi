from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ScreenShotTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Success", "ErrMsg", "Url", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Success: bool
    ErrMsg: str
    Url: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ..., Url: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
