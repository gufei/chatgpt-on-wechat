import CircleNewPublishNotice_pb2 as _CircleNewPublishNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CirclePushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Circles", "Size", "Count", "Page", "RetCode", "RetTips")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    RETCODE_FIELD_NUMBER: _ClassVar[int]
    RETTIPS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Circles: _containers.RepeatedCompositeFieldContainer[_CircleNewPublishNotice_pb2.CircleInformationMessage]
    Size: int
    Count: int
    Page: int
    RetCode: int
    RetTips: str
    def __init__(self, WeChatId: _Optional[str] = ..., Circles: _Optional[_Iterable[_Union[_CircleNewPublishNotice_pb2.CircleInformationMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., RetCode: _Optional[int] = ..., RetTips: _Optional[str] = ...) -> None: ...
