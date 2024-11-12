from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumSettings(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    ChangeNickName: _ClassVar[EnumSettings]
    ChangeAvatar: _ClassVar[EnumSettings]
    NeedVerify: _ClassVar[EnumSettings]
    ChangeGender: _ClassVar[EnumSettings]
    ChangeZone: _ClassVar[EnumSettings]
    ChangeSignature: _ClassVar[EnumSettings]
ChangeNickName: EnumSettings
ChangeAvatar: EnumSettings
NeedVerify: EnumSettings
ChangeGender: EnumSettings
ChangeZone: EnumSettings
ChangeSignature: EnumSettings

class WechatSettingTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Action", "Content", "IntParam", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    ACTION_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    INTPARAM_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Action: EnumSettings
    Content: str
    IntParam: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Action: _Optional[_Union[EnumSettings, str]] = ..., Content: _Optional[str] = ..., IntParam: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
