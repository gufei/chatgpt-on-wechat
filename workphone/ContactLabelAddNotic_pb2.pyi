import ContactLabelInfoNotice_pb2 as _ContactLabelInfoNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContactLabelAddNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Label")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Label: _ContactLabelInfoNotice_pb2.LabelInfoMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Label: _Optional[_Union[_ContactLabelInfoNotice_pb2.LabelInfoMessage, _Mapping]] = ...) -> None: ...
