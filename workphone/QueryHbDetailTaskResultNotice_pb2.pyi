from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class HbRecordMessage(_message.Message):
    __slots__ = ("UserName", "Amount", "Time")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    AMOUNT_FIELD_NUMBER: _ClassVar[int]
    TIME_FIELD_NUMBER: _ClassVar[int]
    UserName: str
    Amount: int
    Time: str
    def __init__(self, UserName: _Optional[str] = ..., Amount: _Optional[int] = ..., Time: _Optional[str] = ...) -> None: ...

class QueryHbDetailTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Success", "ErrMsg", "HbUrl", "TotalNum", "TotalAmount", "RecNum", "RecAmount", "Records", "Sender", "Wishing", "HbType", "HbKind", "HbStatus", "RevStatus")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    HBURL_FIELD_NUMBER: _ClassVar[int]
    TOTALNUM_FIELD_NUMBER: _ClassVar[int]
    TOTALAMOUNT_FIELD_NUMBER: _ClassVar[int]
    RECNUM_FIELD_NUMBER: _ClassVar[int]
    RECAMOUNT_FIELD_NUMBER: _ClassVar[int]
    RECORDS_FIELD_NUMBER: _ClassVar[int]
    SENDER_FIELD_NUMBER: _ClassVar[int]
    WISHING_FIELD_NUMBER: _ClassVar[int]
    HBTYPE_FIELD_NUMBER: _ClassVar[int]
    HBKIND_FIELD_NUMBER: _ClassVar[int]
    HBSTATUS_FIELD_NUMBER: _ClassVar[int]
    REVSTATUS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Success: bool
    ErrMsg: str
    HbUrl: str
    TotalNum: int
    TotalAmount: int
    RecNum: int
    RecAmount: int
    Records: _containers.RepeatedCompositeFieldContainer[HbRecordMessage]
    Sender: str
    Wishing: str
    HbType: int
    HbKind: int
    HbStatus: int
    RevStatus: int
    def __init__(self, WeChatId: _Optional[str] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ..., HbUrl: _Optional[str] = ..., TotalNum: _Optional[int] = ..., TotalAmount: _Optional[int] = ..., RecNum: _Optional[int] = ..., RecAmount: _Optional[int] = ..., Records: _Optional[_Iterable[_Union[HbRecordMessage, _Mapping]]] = ..., Sender: _Optional[str] = ..., Wishing: _Optional[str] = ..., HbType: _Optional[int] = ..., HbKind: _Optional[int] = ..., HbStatus: _Optional[int] = ..., RevStatus: _Optional[int] = ...) -> None: ...
