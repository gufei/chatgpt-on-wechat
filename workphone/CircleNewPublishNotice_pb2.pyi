from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CircleCommentMessage(_message.Message):
    __slots__ = ("CommentId", "ReplyCommentId", "Content", "FromWeChatId", "ToWeChatId", "PublishTime", "FromName", "ToName", "CircleId", "Read")
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    REPLYCOMMENTID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    FROMWECHATID_FIELD_NUMBER: _ClassVar[int]
    TOWECHATID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    FROMNAME_FIELD_NUMBER: _ClassVar[int]
    TONAME_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    CommentId: int
    ReplyCommentId: int
    Content: str
    FromWeChatId: str
    ToWeChatId: str
    PublishTime: int
    FromName: str
    ToName: str
    CircleId: int
    Read: int
    def __init__(self, CommentId: _Optional[int] = ..., ReplyCommentId: _Optional[int] = ..., Content: _Optional[str] = ..., FromWeChatId: _Optional[str] = ..., ToWeChatId: _Optional[str] = ..., PublishTime: _Optional[int] = ..., FromName: _Optional[str] = ..., ToName: _Optional[str] = ..., CircleId: _Optional[int] = ..., Read: _Optional[int] = ...) -> None: ...

class CircleLikeMessage(_message.Message):
    __slots__ = ("FriendId", "PublishTime", "NickName", "CircleId", "Read")
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    READ_FIELD_NUMBER: _ClassVar[int]
    FriendId: str
    PublishTime: int
    NickName: str
    CircleId: int
    Read: int
    def __init__(self, FriendId: _Optional[str] = ..., PublishTime: _Optional[int] = ..., NickName: _Optional[str] = ..., CircleId: _Optional[int] = ..., Read: _Optional[int] = ...) -> None: ...

class CircleInformationMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "Content", "Likes", "Comments", "PublishTime")
    class CircleContentMessage(_message.Message):
        __slots__ = ("Text", "Images", "Link", "Video", "Ext")
        class CircleNewsContentMessage(_message.Message):
            __slots__ = ("ThumbImg", "Url", "Description", "mediaId")
            THUMBIMG_FIELD_NUMBER: _ClassVar[int]
            URL_FIELD_NUMBER: _ClassVar[int]
            DESCRIPTION_FIELD_NUMBER: _ClassVar[int]
            MEDIAID_FIELD_NUMBER: _ClassVar[int]
            ThumbImg: str
            Url: str
            Description: str
            mediaId: str
            def __init__(self, ThumbImg: _Optional[str] = ..., Url: _Optional[str] = ..., Description: _Optional[str] = ..., mediaId: _Optional[str] = ...) -> None: ...
        TEXT_FIELD_NUMBER: _ClassVar[int]
        IMAGES_FIELD_NUMBER: _ClassVar[int]
        LINK_FIELD_NUMBER: _ClassVar[int]
        VIDEO_FIELD_NUMBER: _ClassVar[int]
        EXT_FIELD_NUMBER: _ClassVar[int]
        Text: str
        Images: _containers.RepeatedCompositeFieldContainer[CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage]
        Link: CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage
        Video: CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage
        Ext: str
        def __init__(self, Text: _Optional[str] = ..., Images: _Optional[_Iterable[_Union[CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage, _Mapping]]] = ..., Link: _Optional[_Union[CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage, _Mapping]] = ..., Video: _Optional[_Union[CircleInformationMessage.CircleContentMessage.CircleNewsContentMessage, _Mapping]] = ..., Ext: _Optional[str] = ...) -> None: ...
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    PUBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    Content: CircleInformationMessage.CircleContentMessage
    Likes: _containers.RepeatedCompositeFieldContainer[CircleLikeMessage]
    Comments: _containers.RepeatedCompositeFieldContainer[CircleCommentMessage]
    PublishTime: int
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., Content: _Optional[_Union[CircleInformationMessage.CircleContentMessage, _Mapping]] = ..., Likes: _Optional[_Iterable[_Union[CircleLikeMessage, _Mapping]]] = ..., Comments: _Optional[_Iterable[_Union[CircleCommentMessage, _Mapping]]] = ..., PublishTime: _Optional[int] = ...) -> None: ...

class CircleNewPublishNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Circle")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLE_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Circle: CircleInformationMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Circle: _Optional[_Union[CircleInformationMessage, _Mapping]] = ...) -> None: ...
