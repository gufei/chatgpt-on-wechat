from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CircleCommentDeleteTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "CommentId", "PublishTime", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    PUBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    CommentId: int
    PublishTime: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., CommentId: _Optional[int] = ..., PublishTime: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
