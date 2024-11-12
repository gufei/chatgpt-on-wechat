from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class LabelInfoMessage(_message.Message):
    __slots__ = ("LabelId", "LabelName", "CreateTime")
    LABELID_FIELD_NUMBER: _ClassVar[int]
    LABELNAME_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    LabelId: int
    LabelName: str
    CreateTime: int
    def __init__(self, LabelId: _Optional[int] = ..., LabelName: _Optional[str] = ..., CreateTime: _Optional[int] = ...) -> None: ...

class ContactLabelInfoNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Labels")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    LABELS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Labels: _containers.RepeatedCompositeFieldContainer[LabelInfoMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., Labels: _Optional[_Iterable[_Union[LabelInfoMessage, _Mapping]]] = ...) -> None: ...
