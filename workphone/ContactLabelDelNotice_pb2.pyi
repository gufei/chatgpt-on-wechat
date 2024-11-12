from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ContactLabelDelNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "LabelId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    LABELID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    LabelId: int
    def __init__(self, WeChatId: _Optional[str] = ..., LabelId: _Optional[int] = ...) -> None: ...
