from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CDNDownloadResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Success", "ErrMsg", "FileId", "MsgSvrId", "Url")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    FILEID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    URL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Success: bool
    ErrMsg: str
    FileId: str
    MsgSvrId: int
    Url: str
    def __init__(self, WeChatId: _Optional[str] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ..., FileId: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., Url: _Optional[str] = ...) -> None: ...
