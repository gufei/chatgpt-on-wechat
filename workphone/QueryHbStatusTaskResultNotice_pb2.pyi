from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class QueryHbStatusTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Success", "ErrMsg", "HbUrl", "HbType", "HbStatus", "RevStatus", "StatusMsg")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    HBURL_FIELD_NUMBER: _ClassVar[int]
    HBTYPE_FIELD_NUMBER: _ClassVar[int]
    HBSTATUS_FIELD_NUMBER: _ClassVar[int]
    REVSTATUS_FIELD_NUMBER: _ClassVar[int]
    STATUSMSG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Success: bool
    ErrMsg: str
    HbUrl: str
    HbType: int
    HbStatus: int
    RevStatus: int
    StatusMsg: str
    def __init__(self, WeChatId: _Optional[str] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ..., HbUrl: _Optional[str] = ..., HbType: _Optional[int] = ..., HbStatus: _Optional[int] = ..., RevStatus: _Optional[int] = ..., StatusMsg: _Optional[str] = ...) -> None: ...
