from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SmsMessage(_message.Message):
    __slots__ = ("Id", "Number", "Type", "Date", "Content", "Read", "ThreadId", "SimId", "BlockType")
    ID_FIELD_NUMBER: _ClassVar[int]
    NUMBER_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    DATE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    THREADID_FIELD_NUMBER: _ClassVar[int]
    SIMID_FIELD_NUMBER: _ClassVar[int]
    BLOCKTYPE_FIELD_NUMBER: _ClassVar[int]
    Id: int
    Number: str
    Type: int
    Date: int
    Content: str
    Read: bool
    ThreadId: int
    SimId: int
    BlockType: int
    def __init__(self, Id: _Optional[int] = ..., Number: _Optional[str] = ..., Type: _Optional[int] = ..., Date: _Optional[int] = ..., Content: _Optional[str] = ..., Read: bool = ..., ThreadId: _Optional[int] = ..., SimId: _Optional[int] = ..., BlockType: _Optional[int] = ...) -> None: ...

class SmsPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "Messages")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    MESSAGES_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    Messages: SmsMessage
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., Messages: _Optional[_Union[SmsMessage, _Mapping]] = ...) -> None: ...
