from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardMessageTaskMessage(_message.Message):
    __slots__ = ("MsgSrvId", "WeChatId", "FriendIds", "ExtMsg", "Talker", "TaskId")
    MSGSRVID_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDIDS_FIELD_NUMBER: _ClassVar[int]
    EXTMSG_FIELD_NUMBER: _ClassVar[int]
    TALKER_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    MsgSrvId: int
    WeChatId: str
    FriendIds: str
    ExtMsg: str
    Talker: str
    TaskId: int
    def __init__(self, MsgSrvId: _Optional[int] = ..., WeChatId: _Optional[str] = ..., FriendIds: _Optional[str] = ..., ExtMsg: _Optional[str] = ..., Talker: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
