from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardMultiMessageTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Talker", "FriendIds", "MsgIds", "ExtMsg", "SendRecord", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TALKER_FIELD_NUMBER: _ClassVar[int]
    FRIENDIDS_FIELD_NUMBER: _ClassVar[int]
    MSGIDS_FIELD_NUMBER: _ClassVar[int]
    EXTMSG_FIELD_NUMBER: _ClassVar[int]
    SENDRECORD_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Talker: str
    FriendIds: str
    MsgIds: _containers.RepeatedScalarFieldContainer[int]
    ExtMsg: str
    SendRecord: bool
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Talker: _Optional[str] = ..., FriendIds: _Optional[str] = ..., MsgIds: _Optional[_Iterable[int]] = ..., ExtMsg: _Optional[str] = ..., SendRecord: bool = ..., TaskId: _Optional[int] = ...) -> None: ...
