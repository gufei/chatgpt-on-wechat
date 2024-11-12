from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class JoinGroupByQrTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "QrUrl", "QrContent", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    QRURL_FIELD_NUMBER: _ClassVar[int]
    QRCONTENT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    QrUrl: str
    QrContent: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., QrUrl: _Optional[str] = ..., QrContent: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
