from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class BizContactMessage(_message.Message):
    __slots__ = ("Username", "Alias", "Nickname", "Avatar", "Icon", "Desc", "Company")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    ALIAS_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    AVATAR_FIELD_NUMBER: _ClassVar[int]
    ICON_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    COMPANY_FIELD_NUMBER: _ClassVar[int]
    Username: str
    Alias: str
    Nickname: str
    Avatar: str
    Icon: str
    Desc: str
    Company: str
    def __init__(self, Username: _Optional[str] = ..., Alias: _Optional[str] = ..., Nickname: _Optional[str] = ..., Avatar: _Optional[str] = ..., Icon: _Optional[str] = ..., Desc: _Optional[str] = ..., Company: _Optional[str] = ...) -> None: ...

class BizContactPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Contacts", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTACTS_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Contacts: _containers.RepeatedCompositeFieldContainer[BizContactMessage]
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Contacts: _Optional[_Iterable[_Union[BizContactMessage, _Mapping]]] = ..., TaskId: _Optional[int] = ...) -> None: ...
