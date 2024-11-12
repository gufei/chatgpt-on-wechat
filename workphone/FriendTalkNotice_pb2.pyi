import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendTalkNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "ContentType", "Content", "MsgId", "msgSvrId", "Ext", "CreateTime", "NickName")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    EXT_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    ContentType: _TransportMessage_pb2.EnumContentType
    Content: bytes
    MsgId: int
    msgSvrId: int
    Ext: str
    CreateTime: int
    NickName: str
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., ContentType: _Optional[_Union[_TransportMessage_pb2.EnumContentType, str]] = ..., Content: _Optional[bytes] = ..., MsgId: _Optional[int] = ..., msgSvrId: _Optional[int] = ..., Ext: _Optional[str] = ..., CreateTime: _Optional[int] = ..., NickName: _Optional[str] = ...) -> None: ...
