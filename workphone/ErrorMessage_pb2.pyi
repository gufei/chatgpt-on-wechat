import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ErrorMessage(_message.Message):
    __slots__ = ("ErrorCode", "ErrorMsg")
    ERRORCODE_FIELD_NUMBER: _ClassVar[int]
    ERRORMSG_FIELD_NUMBER: _ClassVar[int]
    ErrorCode: _TransportMessage_pb2.EnumErrorCode
    ErrorMsg: str
    def __init__(self, ErrorCode: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrorMsg: _Optional[str] = ...) -> None: ...
