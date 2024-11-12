from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAuthReqMessage(_message.Message):
    __slots__ = ("AuthType", "Credential")
    class EnumAuthType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Default: _ClassVar[DeviceAuthReqMessage.EnumAuthType]
        DeviceCode: _ClassVar[DeviceAuthReqMessage.EnumAuthType]
        Username: _ClassVar[DeviceAuthReqMessage.EnumAuthType]
        InternalCode: _ClassVar[DeviceAuthReqMessage.EnumAuthType]
    Default: DeviceAuthReqMessage.EnumAuthType
    DeviceCode: DeviceAuthReqMessage.EnumAuthType
    Username: DeviceAuthReqMessage.EnumAuthType
    InternalCode: DeviceAuthReqMessage.EnumAuthType
    AUTHTYPE_FIELD_NUMBER: _ClassVar[int]
    CREDENTIAL_FIELD_NUMBER: _ClassVar[int]
    AuthType: DeviceAuthReqMessage.EnumAuthType
    Credential: str
    def __init__(self, AuthType: _Optional[_Union[DeviceAuthReqMessage.EnumAuthType, str]] = ..., Credential: _Optional[str] = ...) -> None: ...
