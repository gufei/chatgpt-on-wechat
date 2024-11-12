from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumPhoneAction(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    None: _ClassVar[EnumPhoneAction]
    Reboot: _ClassVar[EnumPhoneAction]
    UploadLog: _ClassVar[EnumPhoneAction]
    UploadFile: _ClassVar[EnumPhoneAction]
    CleanAppCache: _ClassVar[EnumPhoneAction]
    CleanWxCache: _ClassVar[EnumPhoneAction]
    CleanFileUrlCache: _ClassVar[EnumPhoneAction]
    PhoneCall: _ClassVar[EnumPhoneAction]
    RestartWx: _ClassVar[EnumPhoneAction]
None: EnumPhoneAction
Reboot: EnumPhoneAction
UploadLog: EnumPhoneAction
UploadFile: EnumPhoneAction
CleanAppCache: EnumPhoneAction
CleanWxCache: EnumPhoneAction
CleanFileUrlCache: EnumPhoneAction
PhoneCall: EnumPhoneAction
RestartWx: EnumPhoneAction

class PhoneActionTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Imei", "Action", "StrParam", "IntParam", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    STRPARAM_FIELD_NUMBER: _ClassVar[int]
    INTPARAM_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Imei: str
    Action: EnumPhoneAction
    StrParam: str
    IntParam: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Imei: _Optional[str] = ..., Action: _Optional[_Union[EnumPhoneAction, str]] = ..., StrParam: _Optional[str] = ..., IntParam: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
