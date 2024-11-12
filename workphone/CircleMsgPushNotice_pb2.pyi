import CircleNewPublishNotice_pb2 as _CircleNewPublishNotice_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CircleMsgPushNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Comments", "Likes", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    COMMENTS_FIELD_NUMBER: _ClassVar[int]
    LIKES_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Comments: _containers.RepeatedCompositeFieldContainer[_CircleNewPublishNotice_pb2.CircleCommentMessage]
    Likes: _containers.RepeatedCompositeFieldContainer[_CircleNewPublishNotice_pb2.CircleLikeMessage]
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Comments: _Optional[_Iterable[_Union[_CircleNewPublishNotice_pb2.CircleCommentMessage, _Mapping]]] = ..., Likes: _Optional[_Iterable[_Union[_CircleNewPublishNotice_pb2.CircleLikeMessage, _Mapping]]] = ..., TaskId: _Optional[int] = ...) -> None: ...
