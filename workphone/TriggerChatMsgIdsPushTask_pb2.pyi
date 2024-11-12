from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class TriggerChatMsgIdsPushTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "StartTime", "EndTime")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    StartTime: int
    EndTime: int
    def __init__(self, WeChatId: _Optional[str] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ...) -> None: ...
