from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMsgFilePushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "MsgSvrId", "MsgType", "Url", "FileSize", "SubType")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    FILESIZE_FIELD_NUMBER: _ClassVar[int]
    SUBTYPE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    MsgSvrId: int
    MsgType: int
    Url: str
    FileSize: int
    SubType: int
    def __init__(self, WeChatId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., MsgType: _Optional[int] = ..., Url: _Optional[str] = ..., FileSize: _Optional[int] = ..., SubType: _Optional[int] = ...) -> None: ...
