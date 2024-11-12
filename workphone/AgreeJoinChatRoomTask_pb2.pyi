from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AgreeJoinChatRoomTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Talker", "MsgSvrId", "MsgContent", "taskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    TALKER_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MSGCONTENT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Talker: str
    MsgSvrId: int
    MsgContent: str
    taskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Talker: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., MsgContent: _Optional[str] = ..., taskId: _Optional[int] = ...) -> None: ...
