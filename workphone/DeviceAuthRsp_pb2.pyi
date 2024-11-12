import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAuthRspMessage(_message.Message):
    __slots__ = ("AccessToken", "Extra")
    class ExtraMessage(_message.Message):
        __slots__ = ("SupplierId", "UnionId", "AccountType", "SupplierName", "NickName", "Token")
        SUPPLIERID_FIELD_NUMBER: _ClassVar[int]
        UNIONID_FIELD_NUMBER: _ClassVar[int]
        ACCOUNTTYPE_FIELD_NUMBER: _ClassVar[int]
        SUPPLIERNAME_FIELD_NUMBER: _ClassVar[int]
        NICKNAME_FIELD_NUMBER: _ClassVar[int]
        TOKEN_FIELD_NUMBER: _ClassVar[int]
        SupplierId: int
        UnionId: int
        AccountType: _TransportMessage_pb2.EnumAccountType
        SupplierName: str
        NickName: str
        Token: str
        def __init__(self, SupplierId: _Optional[int] = ..., UnionId: _Optional[int] = ..., AccountType: _Optional[_Union[_TransportMessage_pb2.EnumAccountType, str]] = ..., SupplierName: _Optional[str] = ..., NickName: _Optional[str] = ..., Token: _Optional[str] = ...) -> None: ...
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    AccessToken: str
    Extra: DeviceAuthRspMessage.ExtraMessage
    def __init__(self, AccessToken: _Optional[str] = ..., Extra: _Optional[_Union[DeviceAuthRspMessage.ExtraMessage, _Mapping]] = ...) -> None: ...
