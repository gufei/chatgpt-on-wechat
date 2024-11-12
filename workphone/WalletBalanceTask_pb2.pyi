from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class WalletBalanceTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Flag")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FLAG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Flag: int
    def __init__(self, WeChatId: _Optional[str] = ..., Flag: _Optional[int] = ...) -> None: ...
