from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendSmsTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Imei", "Number", "Content", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Imei: str
    Number: str
    Content: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Imei: _Optional[str] = ..., Number: _Optional[str] = ..., Content: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
