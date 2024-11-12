import ConfigPushNotice_pb2 as _ConfigPushNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class SetConfigTaskMessage(_message.Message):
    __slots__ = ("IMEI", "WeChatId", "BoolConfs", "IntConfs", "StrConfs")
    IMEI_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    BOOLCONFS_FIELD_NUMBER: _ClassVar[int]
    INTCONFS_FIELD_NUMBER: _ClassVar[int]
    STRCONFS_FIELD_NUMBER: _ClassVar[int]
    IMEI: str
    WeChatId: str
    BoolConfs: _containers.RepeatedCompositeFieldContainer[_ConfigPushNotice_pb2.BoolConfigMessage]
    IntConfs: _containers.RepeatedCompositeFieldContainer[_ConfigPushNotice_pb2.IntConfigMessage]
    StrConfs: _containers.RepeatedCompositeFieldContainer[_ConfigPushNotice_pb2.StrConfigMessage]
    def __init__(self, IMEI: _Optional[str] = ..., WeChatId: _Optional[str] = ..., BoolConfs: _Optional[_Iterable[_Union[_ConfigPushNotice_pb2.BoolConfigMessage, _Mapping]]] = ..., IntConfs: _Optional[_Iterable[_Union[_ConfigPushNotice_pb2.IntConfigMessage, _Mapping]]] = ..., StrConfs: _Optional[_Iterable[_Union[_ConfigPushNotice_pb2.StrConfigMessage, _Mapping]]] = ...) -> None: ...
