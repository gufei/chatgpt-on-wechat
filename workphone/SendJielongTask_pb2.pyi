from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class SendJielongTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Chatoom", "Content", "Title", "Sample", "Memo", "MsgSvrId", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATOOM_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    SAMPLE_FIELD_NUMBER: _ClassVar[int]
    MEMO_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Chatoom: str
    Content: str
    Title: str
    Sample: str
    Memo: str
    MsgSvrId: int
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Chatoom: _Optional[str] = ..., Content: _Optional[str] = ..., Title: _Optional[str] = ..., Sample: _Optional[str] = ..., Memo: _Optional[str] = ..., MsgSvrId: _Optional[int] = ..., TaskId: _Optional[int] = ...) -> None: ...
