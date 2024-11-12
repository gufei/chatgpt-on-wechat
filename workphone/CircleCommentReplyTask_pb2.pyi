from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CircleCommentReplyTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "ToWeChatId", "Content", "ReplyCommentId", "TaskId", "IsResend")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    TOWECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REPLYCOMMENTID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    ISRESEND_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    ToWeChatId: str
    Content: str
    ReplyCommentId: int
    TaskId: int
    IsResend: bool
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., ToWeChatId: _Optional[str] = ..., Content: _Optional[str] = ..., ReplyCommentId: _Optional[int] = ..., TaskId: _Optional[int] = ..., IsResend: bool = ...) -> None: ...
