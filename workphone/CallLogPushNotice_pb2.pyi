from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CallLogMessage(_message.Message):
    __slots__ = ("Id", "Number", "Type", "Date", "Duration", "Record", "SimId", "BlockType")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    RECORD_FIELD_NUMBER: _ClassVar[int]
    SIMID_FIELD_NUMBER: _ClassVar[int]
    BLOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Number: str
    Type: int
    Date: int
    Duration: int
    Record: str
    SimId: int
    BlockType: int
    def __init__(self, Id: _Optional[int] = ..., Number: _Optional[str] = ..., Type: _Optional[int] = ..., Date: _Optional[int] = ..., Duration: _Optional[int] = ..., Record: _Optional[str] = ..., SimId: _Optional[int] = ..., BlockType: _Optional[int] = ...) -> None: ...

class CallLogPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "Messages")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    Messages: CallLogMessage
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., Messages: _Optional[_Union[CallLogMessage, _Mapping]] = ...) -> None: ...
