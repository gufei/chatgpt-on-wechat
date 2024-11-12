import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TakeMoneyTaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "Code", "ErrMsg", "TaskId", "MsgKey", "Amount", "WeChatId", "Sender", "Type", "SenderName")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    MSGKEY_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    SENDERNAME_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Code: _TransportMessage_pb2.EnumErrorCode
    ErrMsg: str
    TaskId: int
    MsgKey: str
    Amount: int
    WeChatId: str
    Sender: str
    Type: int
    SenderName: str
    def __init__(self, Success: bool = ..., Code: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrMsg: _Optional[str] = ..., TaskId: _Optional[int] = ..., MsgKey: _Optional[str] = ..., Amount: _Optional[int] = ..., WeChatId: _Optional[str] = ..., Sender: _Optional[str] = ..., Type: _Optional[int] = ..., SenderName: _Optional[str] = ...) -> None: ...
