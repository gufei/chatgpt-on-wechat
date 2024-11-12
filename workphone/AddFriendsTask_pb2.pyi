from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddFriendsTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Phones", "message", "TaskId", "Label", "Remark", "FiledStr1", "FiledStr2", "FiledStr3", "CustomId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    PHONES_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    FILEDSTR1_FIELD_NUMBER: _ClassVar[int]
    FILEDSTR2_FIELD_NUMBER: _ClassVar[int]
    FILEDSTR3_FIELD_NUMBER: _ClassVar[int]
    CUSTOMID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Phones: _containers.RepeatedScalarFieldContainer[str]
    message: str
    TaskId: int
    Label: str
    Remark: str
    FiledStr1: str
    FiledStr2: str
    FiledStr3: str
    CustomId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Phones: _Optional[_Iterable[str]] = ..., message: _Optional[str] = ..., TaskId: _Optional[int] = ..., Label: _Optional[str] = ..., Remark: _Optional[str] = ..., FiledStr1: _Optional[str] = ..., FiledStr2: _Optional[str] = ..., FiledStr3: _Optional[str] = ..., CustomId: _Optional[int] = ...) -> None: ...
