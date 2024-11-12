import CircleNewPublishNotice_pb2 as _CircleNewPublishNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CircleDetailNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Circle")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Circle: _CircleNewPublishNotice_pb2.CircleInformationMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Circle: _Optional[_Union[_CircleNewPublishNotice_pb2.CircleInformationMessage, _Mapping]] = ...) -> None: ...
