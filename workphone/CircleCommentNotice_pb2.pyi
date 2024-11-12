import CircleNewPublishNotice_pb2 as _CircleNewPublishNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CircleCommentNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "IsDelete", "Comment")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    ISDELETE_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    IsDelete: bool
    Comment: _CircleNewPublishNotice_pb2.CircleCommentMessage
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., IsDelete: bool = ..., Comment: _Optional[_Union[_CircleNewPublishNotice_pb2.CircleCommentMessage, _Mapping]] = ...) -> None: ...
