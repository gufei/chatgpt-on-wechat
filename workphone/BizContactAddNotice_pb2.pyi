import BizContactPushNotice_pb2 as _BizContactPushNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BizContactAddNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Contact")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Contact: _BizContactPushNotice_pb2.BizContactMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Contact: _Optional[_Union[_BizContactPushNotice_pb2.BizContactMessage, _Mapping]] = ...) -> None: ...
