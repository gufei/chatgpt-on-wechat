import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class GetWeChatsReqMessage(_message.Message):
    __slots__ = ("UnionId", "AccountType")
    UNIONID_FIELD_NUMBER: _ClassVar[int]
    ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
    UnionId: int
    AccountType: _TransportMessage_pb2.EnumAccountType
    def __init__(self, UnionId: _Optional[int] = ..., AccountType: _Optional[_Union[_TransportMessage_pb2.EnumAccountType, str]] = ...) -> None: ...
