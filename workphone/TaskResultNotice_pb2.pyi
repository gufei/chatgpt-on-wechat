import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "Code", "ErrMsg", "TaskId", "TaskType", "WeChatId")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    TASKTYPE_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Code: _TransportMessage_pb2.EnumErrorCode
    ErrMsg: str
    TaskId: int
    TaskType: _TransportMessage_pb2.EnumMsgType
    WeChatId: str
    def __init__(self, Success: bool = ..., Code: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrMsg: _Optional[str] = ..., TaskId: _Optional[int] = ..., TaskType: _Optional[_Union[_TransportMessage_pb2.EnumMsgType, str]] = ..., WeChatId: _Optional[str] = ...) -> None: ...
