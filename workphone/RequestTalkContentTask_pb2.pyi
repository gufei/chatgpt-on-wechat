from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestTalkContentTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "MsgSvrId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    MsgSvrId: int
    def __init__(self, WeChatId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ...) -> None: ...
