from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMsgIdsPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "StartTime", "EndTime", "Ids")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    STARTTIME_FIELD_NUMBER: _ClassVar[int]
    ENDTIME_FIELD_NUMBER: _ClassVar[int]
    IDS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    StartTime: int
    EndTime: int
    Ids: _containers.RepeatedScalarFieldContainer[int]
    def __init__(self, WeChatId: _Optional[str] = ..., StartTime: _Optional[int] = ..., EndTime: _Optional[int] = ..., Ids: _Optional[_Iterable[int]] = ...) -> None: ...
