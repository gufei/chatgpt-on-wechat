from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddFriendFromPhonebookTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Count", "Reset", "Message", "TaskId", "Index")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    RESET_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    INDEX_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Count: int
    Reset: bool
    Message: str
    TaskId: int
    Index: int
    def __init__(self, WeChatId: _Optional[str] = ..., Count: _Optional[int] = ..., Reset: bool = ..., Message: _Optional[str] = ..., TaskId: _Optional[int] = ..., Index: _Optional[int] = ...) -> None: ...
