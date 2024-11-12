from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostSNSNewsTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Content", "Attachment", "Comment", "TaskId", "Visible", "SendSlow", "Poi", "ExtComment")
    class AttachmentMessage(_message.Message):
        __slots__ = ("Type", "Content")
        class EnumAttachType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Link: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
            Picture: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
            ShortVideo: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
            LongVideo: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
            ShiPinHao: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
            ExtLink: _ClassVar[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType]
        Link: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        Picture: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        ShortVideo: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        LongVideo: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        ShiPinHao: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        ExtLink: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        CONTENT_FIELD_NUMBER: _ClassVar[int]
        Type: PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType
        Content: _containers.RepeatedScalarFieldContainer[str]
        def __init__(self, Type: _Optional[_Union[PostSNSNewsTaskMessage.AttachmentMessage.EnumAttachType, str]] = ..., Content: _Optional[_Iterable[str]] = ...) -> None: ...
    class VisibleMessage(_message.Message):
        __slots__ = ("Type", "Labels", "Friends")
        class EnumVisibleType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
            __slots__ = ()
            Public: _ClassVar[PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType]
            Private: _ClassVar[PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType]
            WhoVisible: _ClassVar[PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType]
            WhoInvisible: _ClassVar[PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType]
        Public: PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType
        Private: PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType
        WhoVisible: PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType
        WhoInvisible: PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType
        TYPE_FIELD_NUMBER: _ClassVar[int]
        LABELS_FIELD_NUMBER: _ClassVar[int]
        FRIENDS_FIELD_NUMBER: _ClassVar[int]
        Type: PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType
        Labels: str
        Friends: str
        def __init__(self, Type: _Optional[_Union[PostSNSNewsTaskMessage.VisibleMessage.EnumVisibleType, str]] = ..., Labels: _Optional[str] = ..., Friends: _Optional[str] = ...) -> None: ...
    class PoiMessage(_message.Message):
        __slots__ = ("City", "Name", "Address", "Lat", "Lng")
        CITY_FIELD_NUMBER: _ClassVar[int]
        NAME_FIELD_NUMBER: _ClassVar[int]
        ADDRESS_FIELD_NUMBER: _ClassVar[int]
        LAT_FIELD_NUMBER: _ClassVar[int]
        LNG_FIELD_NUMBER: _ClassVar[int]
        City: str
        Name: str
        Address: str
        Lat: float
        Lng: float
        def __init__(self, City: _Optional[str] = ..., Name: _Optional[str] = ..., Address: _Optional[str] = ..., Lat: _Optional[float] = ..., Lng: _Optional[float] = ...) -> None: ...
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    ATTACHMENT_FIELD_NUMBER: _ClassVar[int]
    COMMENT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    VISIBLE_FIELD_NUMBER: _ClassVar[int]
    SENDSLOW_FIELD_NUMBER: _ClassVar[int]
    POI_FIELD_NUMBER: _ClassVar[int]
    EXTCOMMENT_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Content: str
    Attachment: PostSNSNewsTaskMessage.AttachmentMessage
    Comment: str
    TaskId: int
    Visible: PostSNSNewsTaskMessage.VisibleMessage
    SendSlow: bool
    Poi: PostSNSNewsTaskMessage.PoiMessage
    ExtComment: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, WeChatId: _Optional[str] = ..., Content: _Optional[str] = ..., Attachment: _Optional[_Union[PostSNSNewsTaskMessage.AttachmentMessage, _Mapping]] = ..., Comment: _Optional[str] = ..., TaskId: _Optional[int] = ..., Visible: _Optional[_Union[PostSNSNewsTaskMessage.VisibleMessage, _Mapping]] = ..., SendSlow: bool = ..., Poi: _Optional[_Union[PostSNSNewsTaskMessage.PoiMessage, _Mapping]] = ..., ExtComment: _Optional[_Iterable[str]] = ...) -> None: ...
