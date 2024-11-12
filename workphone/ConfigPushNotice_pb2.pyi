from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BoolConfigMessage(_message.Message):
    __slots__ = ("Key", "Value", "Name", "Desc")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Value: bool
    Name: str
    Desc: str
    def __init__(self, Key: _Optional[str] = ..., Value: bool = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ...) -> None: ...

class IntConfigMessage(_message.Message):
    __slots__ = ("Key", "Value", "Name", "Desc")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Value: int
    Name: str
    Desc: str
    def __init__(self, Key: _Optional[str] = ..., Value: _Optional[int] = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ...) -> None: ...

class StrConfigMessage(_message.Message):
    __slots__ = ("Key", "Value", "Name", "Desc")
    KEY_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    Key: str
    Value: str
    Name: str
    Desc: str
    def __init__(self, Key: _Optional[str] = ..., Value: _Optional[str] = ..., Name: _Optional[str] = ..., Desc: _Optional[str] = ...) -> None: ...

class ConfigPushNoticeMessage(_message.Message):
    __slots__ = ("IMEI", "WeChatId", "BoolConfs", "IntConfs", "StrConfs")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    BOOLCONFS_FIELD_NUMBER: _ClassVar[int]
    INTCONFS_FIELD_NUMBER: _ClassVar[int]
    STRCONFS_FIELD_NUMBER: _ClassVar[int]
    IMEI: str
    WeChatId: str
    BoolConfs: _containers.RepeatedCompositeFieldContainer[BoolConfigMessage]
    IntConfs: _containers.RepeatedCompositeFieldContainer[IntConfigMessage]
    StrConfs: _containers.RepeatedCompositeFieldContainer[StrConfigMessage]
    def __init__(self, IMEI: _Optional[str] = ..., WeChatId: _Optional[str] = ..., BoolConfs: _Optional[_Iterable[_Union[BoolConfigMessage, _Mapping]]] = ..., IntConfs: _Optional[_Iterable[_Union[IntConfigMessage, _Mapping]]] = ..., StrConfs: _Optional[_Iterable[_Union[StrConfigMessage, _Mapping]]] = ...) -> None: ...
