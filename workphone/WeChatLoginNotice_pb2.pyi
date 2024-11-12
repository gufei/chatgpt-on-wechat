import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatLoginNoticeMessage(_message.Message):
    __slots__ = ("SupplierId", "UnionId", "AccountType", "WeChats")
    class WeChatLoginMessage(_message.Message):
        __slots__ = ("WeChatId", "IsLogin")
        WECHATID_FIELD_NUMBER: _ClassVar[int]
        ISLOGIN_FIELD_NUMBER: _ClassVar[int]
        WeChatId: str
        IsLogin: bool
        def __init__(self, WeChatId: _Optional[str] = ..., IsLogin: bool = ...) -> None: ...
    SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
    UNIONID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    WECHATS_FIELD_NUMBER: _ClassVar[int]
    SupplierId: int
    UnionId: int
    AccountType: _TransportMessage_pb2.EnumAccountType
    WeChats: _containers.RepeatedCompositeFieldContainer[WeChatLoginNoticeMessage.WeChatLoginMessage]
    def __init__(self, SupplierId: _Optional[int] = ..., UnionId: _Optional[int] = ..., AccountType: _Optional[_Union[_TransportMessage_pb2.EnumAccountType, str]] = ..., WeChats: _Optional[_Iterable[_Union[WeChatLoginNoticeMessage.WeChatLoginMessage, _Mapping]]] = ...) -> None: ...
