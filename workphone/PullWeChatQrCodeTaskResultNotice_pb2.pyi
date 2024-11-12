from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class PullWeChatQrCodeTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "QrCodeUrl", "Success", "ErrMsg")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    QRCODEURL_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    QrCodeUrl: str
    Success: bool
    ErrMsg: str
    def __init__(self, WeChatId: _Optional[str] = ..., QrCodeUrl: _Optional[str] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ...) -> None: ...
