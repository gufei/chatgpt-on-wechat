from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class AddFriendWithSceneTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Friend", "Message", "Scene", "Remark", "TaskId", "Label")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    SCENE_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    LABEL_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Friend: str
    Message: str
    Scene: int
    Remark: str
    TaskId: int
    Label: str
    def __init__(self, WeChatId: _Optional[str] = ..., Friend: _Optional[str] = ..., Message: _Optional[str] = ..., Scene: _Optional[int] = ..., Remark: _Optional[str] = ..., TaskId: _Optional[int] = ..., Label: _Optional[str] = ...) -> None: ...
