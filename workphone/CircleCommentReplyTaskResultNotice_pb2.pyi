import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CircleCommentReplyTaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "Code", "ErrMsg", "CommentId", "ReplyCommentId", "TaskId", "PusblishTime", "CircleId", "WeChatId")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    COMMENTID_FIELD_NUMBER: _ClassVar[int]
    REPLYCOMMENTID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    PUSBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Code: _TransportMessage_pb2.EnumErrorCode
    ErrMsg: str
    CommentId: int
    ReplyCommentId: int
    TaskId: int
    PusblishTime: int
    CircleId: int
    WeChatId: str
    def __init__(self, Success: bool = ..., Code: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrMsg: _Optional[str] = ..., CommentId: _Optional[int] = ..., ReplyCommentId: _Optional[int] = ..., TaskId: _Optional[int] = ..., PusblishTime: _Optional[int] = ..., CircleId: _Optional[int] = ..., WeChatId: _Optional[str] = ...) -> None: ...
