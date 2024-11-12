import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class RequestTalkMsgTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "ContentType", "Content", "MsgSvrId", "IsSend", "CreateTime", "Status")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    ContentType: _TransportMessage_pb2.EnumContentType
    Content: bytes
    MsgSvrId: int
    IsSend: bool
    CreateTime: int
    Status: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., ContentType: _Optional[_Union[_TransportMessage_pb2.EnumContentType, str]] = ..., Content: _Optional[bytes] = ..., MsgSvrId: _Optional[int] = ..., IsSend: bool = ..., CreateTime: _Optional[int] = ..., Status: _Optional[int] = ...) -> None: ...
