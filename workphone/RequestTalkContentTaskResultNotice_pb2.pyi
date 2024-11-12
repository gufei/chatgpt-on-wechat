from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestTalkContentTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "MsgSvrId", "MsgType", "Content")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    MsgSvrId: int
    MsgType: int
    Content: str
    def __init__(self, WeChatId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., MsgType: _Optional[int] = ..., Content: _Optional[str] = ...) -> None: ...
