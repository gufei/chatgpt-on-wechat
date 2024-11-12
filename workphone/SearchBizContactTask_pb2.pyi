from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SearchBizContactTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "KeyWord", "Type", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    KeyWord: str
    Type: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., KeyWord: _Optional[str] = ..., Type: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
