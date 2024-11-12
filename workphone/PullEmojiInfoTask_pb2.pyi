from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullEmojiInfoTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Md5", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Md5: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Md5: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
