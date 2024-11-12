from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ForwardMessageByContentTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendIds", "MsgSvrId", "MsgType", "Content", "TaskId", "Thumb")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDIDS_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    THUMB_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendIds: str
    MsgSvrId: int
    MsgType: int
    Content: str
    TaskId: int
    Thumb: str
    def __init__(self, WeChatId: _Optional[str] = ..., FriendIds: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., MsgType: _Optional[int] = ..., Content: _Optional[str] = ..., TaskId: _Optional[int] = ..., Thumb: _Optional[str] = ...) -> None: ...
