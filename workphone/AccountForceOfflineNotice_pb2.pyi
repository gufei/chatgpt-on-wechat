import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AccountForceOfflineNoticeMessage(_message.Message):
    __slots__ = ("Reason", "Message", "WeChatId")
    REASON_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    Reason: _TransportMessage_pb2.EnumForceOfflineReason
    Message: str
    WeChatId: str
    def __init__(self, Reason: _Optional[_Union[_TransportMessage_pb2.EnumForceOfflineReason, str]] = ..., Message: _Optional[str] = ..., WeChatId: _Optional[str] = ...) -> None: ...
