from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class WeChatGroupSendTaskMessage(_message.Message):
    __slots__ = ("TaskId", "FriendIds", "ContentType", "Content", "WeChatId", "Duration", "Original")
    class EnumGroupMsgContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Text: _ClassVar[WeChatGroupSendTaskMessage.EnumGroupMsgContentType]
        Picture: _ClassVar[WeChatGroupSendTaskMessage.EnumGroupMsgContentType]
        Voice: _ClassVar[WeChatGroupSendTaskMessage.EnumGroupMsgContentType]
        Video: _ClassVar[WeChatGroupSendTaskMessage.EnumGroupMsgContentType]
    Text: WeChatGroupSendTaskMessage.EnumGroupMsgContentType
    Picture: WeChatGroupSendTaskMessage.EnumGroupMsgContentType
    Voice: WeChatGroupSendTaskMessage.EnumGroupMsgContentType
    Video: WeChatGroupSendTaskMessage.EnumGroupMsgContentType
    TASKID_FIELD_NUMBER: _ClassVar[int]
    FRIENDIDS_FIELD_NUMBER: _ClassVar[int]
    CONTENTTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    DURATION_FIELD_NUMBER: _ClassVar[int]
    ORIGINAL_FIELD_NUMBER: _ClassVar[int]
    TaskId: int
    FriendIds: _containers.RepeatedScalarFieldContainer[str]
    ContentType: WeChatGroupSendTaskMessage.EnumGroupMsgContentType
    Content: str
    WeChatId: str
    Duration: int
    Original: bool
    def __init__(self, TaskId: _Optional[int] = ..., FriendIds: _Optional[_Iterable[str]] = ..., ContentType: _Optional[_Union[WeChatGroupSendTaskMessage.EnumGroupMsgContentType, str]] = ..., Content: _Optional[str] = ..., WeChatId: _Optional[str] = ..., Duration: _Optional[int] = ..., Original: bool = ...) -> None: ...
