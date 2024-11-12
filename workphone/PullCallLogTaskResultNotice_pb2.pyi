import CallLogPushNotice_pb2 as _CallLogPushNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PullCallLogTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "TaskId", "Success", "Messages", "ErrMsg")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    TaskId: int
    Success: bool
    Messages: _containers.RepeatedCompositeFieldContainer[_CallLogPushNotice_pb2.CallLogMessage]
    ErrMsg: str
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., TaskId: _Optional[int] = ..., Success: bool = ..., Messages: _Optional[_Iterable[_Union[_CallLogPushNotice_pb2.CallLogMessage, _Mapping]]] = ..., ErrMsg: _Optional[str] = ...) -> None: ...
