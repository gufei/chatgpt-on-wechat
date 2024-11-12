import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatMessage(_message.Message):
    __slots__ = ("FriendId", "ContentType", "Content", "MsgId", "MsgSvrId", "IsSend", "CreateTime", "Status")
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    ISSEND_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    STATUS_FIELD_NUMBER: _ClassVar[int]
    FriendId: str
    ContentType: _TransportMessage_pb2.EnumContentType
    Content: bytes
    MsgId: int
    MsgSvrId: int
    IsSend: bool
    CreateTime: int
    Status: int
    def __init__(self, FriendId: _Optional[str] = ..., ContentType: _Optional[_Union[_TransportMessage_pb2.EnumContentType, str]] = ..., Content: _Optional[bytes] = ..., MsgId: _Optional[int] = ..., MsgSvrId: _Optional[int] = ..., IsSend: bool = ..., CreateTime: _Optional[int] = ..., Status: _Optional[int] = ...) -> None: ...

class HistoryMsgPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Messages", "Size", "Count", "Page", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    COUNT_FIELD_NUMBER: _ClassVar[int]
    PAGE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Messages: _containers.RepeatedCompositeFieldContainer[ChatMessage]
    Size: int
    Count: int
    Page: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Messages: _Optional[_Iterable[_Union[ChatMessage, _Mapping]]] = ..., Size: _Optional[int] = ..., Count: _Optional[int] = ..., Page: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
