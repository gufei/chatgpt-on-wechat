from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EmojiMessage(_message.Message):
    __slots__ = ("md5", "cdnUrl", "catalog", "type", "state", "width", "height", "size", "encrypturl", "aeskey", "externUrl", "externMd5", "name", "groupId", "thumbUrl", "desc")
    MD5_FIELD_NUMBER: _ClassVar[int]
    CDNURL_FIELD_NUMBER: _ClassVar[int]
    CATALOG_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    STATE_FIELD_NUMBER: _ClassVar[int]
    WIDTH_FIELD_NUMBER: _ClassVar[int]
    HEIGHT_FIELD_NUMBER: _ClassVar[int]
    SIZE_FIELD_NUMBER: _ClassVar[int]
    ENCRYPTURL_FIELD_NUMBER: _ClassVar[int]
    AESKEY_FIELD_NUMBER: _ClassVar[int]
    EXTERNURL_FIELD_NUMBER: _ClassVar[int]
    EXTERNMD5_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    GROUPID_FIELD_NUMBER: _ClassVar[int]
    THUMBURL_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    md5: str
    cdnUrl: str
    catalog: int
    type: int
    state: int
    width: int
    height: int
    size: int
    encrypturl: str
    aeskey: str
    externUrl: str
    externMd5: str
    name: str
    groupId: str
    thumbUrl: str
    desc: str
    def __init__(self, md5: _Optional[str] = ..., cdnUrl: _Optional[str] = ..., catalog: _Optional[int] = ..., type: _Optional[int] = ..., state: _Optional[int] = ..., width: _Optional[int] = ..., height: _Optional[int] = ..., size: _Optional[int] = ..., encrypturl: _Optional[str] = ..., aeskey: _Optional[str] = ..., externUrl: _Optional[str] = ..., externMd5: _Optional[str] = ..., name: _Optional[str] = ..., groupId: _Optional[str] = ..., thumbUrl: _Optional[str] = ..., desc: _Optional[str] = ...) -> None: ...

class PullEmojiInfoTaskResultNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "TaskId", "Emojis")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    EMOJIS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    TaskId: int
    Emojis: _containers.RepeatedCompositeFieldContainer[EmojiMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., TaskId: _Optional[int] = ..., Emojis: _Optional[_Iterable[_Union[EmojiMessage, _Mapping]]] = ...) -> None: ...
