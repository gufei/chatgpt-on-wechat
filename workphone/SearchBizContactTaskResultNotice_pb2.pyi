import BizContactPushNotice_pb2 as _BizContactPushNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SearchBizContactTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "KeyWord", "Type", "TaskId", "Items")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    KEYWORD_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    ITEMS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    KeyWord: str
    Type: int
    TaskId: int
    Items: _containers.RepeatedCompositeFieldContainer[_BizContactPushNotice_pb2.BizContactMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., KeyWord: _Optional[str] = ..., Type: _Optional[int] = ..., TaskId: _Optional[int] = ..., Items: _Optional[_Iterable[_Union[_BizContactPushNotice_pb2.BizContactMessage, _Mapping]]] = ...) -> None: ...
