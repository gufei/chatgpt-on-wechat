import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TalkToFriendTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "ContentType", "Content", "Remark", "MsgId", "Immediate")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    IMMEDIATE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    ContentType: _TransportMessage_pb2.EnumContentType
    Content: bytes
    Remark: str
    MsgId: int
    Immediate: bool
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., ContentType: _Optional[_Union[_TransportMessage_pb2.EnumContentType, str]] = ..., Content: _Optional[bytes] = ..., Remark: _Optional[str] = ..., MsgId: _Optional[int] = ..., Immediate: bool = ...) -> None: ...
