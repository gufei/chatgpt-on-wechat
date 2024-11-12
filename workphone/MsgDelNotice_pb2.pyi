import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MsgDelNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "IsSend", "ContentType", "Content", "MsgId", "msgSvrId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    IsSend: bool
    ContentType: _TransportMessage_pb2.EnumContentType
    Content: bytes
    MsgId: int
    msgSvrId: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., IsSend: bool = ..., ContentType: _Optional[_Union[_TransportMessage_pb2.EnumContentType, str]] = ..., Content: _Optional[bytes] = ..., MsgId: _Optional[int] = ..., msgSvrId: _Optional[int] = ...) -> None: ...
