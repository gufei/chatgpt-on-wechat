from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetContactInfoTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "Contact", "Chatroom", "Ticket", "TaskId")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    CHATROOM_FIELD_NUMBER: _ClassVar[int]
    TICKET_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Contact: str
    Chatroom: str
    Ticket: str
    TaskId: int
    def __init__(self, WeChatId: _Optional[str] = ..., Contact: _Optional[str] = ..., Chatroom: _Optional[str] = ..., Ticket: _Optional[str] = ..., TaskId: _Optional[int] = ...) -> None: ...
