import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostSNSNewsTaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "Code", "ErrMsg", "TaskId", "Extra", "WeChatId")
    class ExtraProperties(_message.Message):
        __slots__ = ("CircleId",)
        CIRCLEID_FIELD_NUMBER: _ClassVar[int]
        CircleId: int
        def __init__(self, CircleId: _Optional[int] = ...) -> None: ...
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    EXTRA_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Code: _TransportMessage_pb2.EnumErrorCode
    ErrMsg: str
    TaskId: int
    Extra: PostSNSNewsTaskResultNoticeMessage.ExtraProperties
    WeChatId: str
    def __init__(self, Success: bool = ..., Code: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrMsg: _Optional[str] = ..., TaskId: _Optional[int] = ..., Extra: _Optional[_Union[PostSNSNewsTaskResultNoticeMessage.ExtraProperties, _Mapping]] = ..., WeChatId: _Optional[str] = ...) -> None: ...
