from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContactLabelTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "LabelName", "LabelId", "AddList", "DelList", "taskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    LABELNAME_FIELD_NUMBER: _ClassVar[int]
    LABELID_FIELD_NUMBER: _ClassVar[int]
    ADDLIST_FIELD_NUMBER: _ClassVar[int]
    DELLIST_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    LabelName: str
    LabelId: int
    AddList: str
    DelList: str
    taskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., LabelName: _Optional[str] = ..., LabelId: _Optional[int] = ..., AddList: _Optional[str] = ..., DelList: _Optional[str] = ..., taskId: _Optional[int] = ...) -> None: ...
