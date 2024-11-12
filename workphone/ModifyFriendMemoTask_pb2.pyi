from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class ModifyFriendMemoTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "Memo", "TaskId", "Desc", "Phone", "DelFlag")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    DESC_FIELD_NUMBER: _ClassVar[int]
    PHONE_FIELD_NUMBER: _ClassVar[int]
    DELFLAG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    Memo: str
    TaskId: int
    Desc: str
    Phone: str
    DelFlag: int
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., Memo: _Optional[str] = ..., TaskId: _Optional[int] = ..., Desc: _Optional[str] = ..., Phone: _Optional[str] = ..., DelFlag: _Optional[int] = ...) -> None: ...
