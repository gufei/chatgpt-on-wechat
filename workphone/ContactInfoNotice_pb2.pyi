import ChatRoomMembersNotice_pb2 as _ChatRoomMembersNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ContactInfoNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Contact", "TaskId", "Success", "ErrMsg")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CONTACT_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Contact: _ChatRoomMembersNotice_pb2.StrangerMessage
    TaskId: int
    Success: bool
    ErrMsg: str
    def __init__(self, WeChatId: _Optional[str] = ..., Contact: _Optional[_Union[_ChatRoomMembersNotice_pb2.StrangerMessage, _Mapping]] = ..., TaskId: _Optional[int] = ..., Success: bool = ..., ErrMsg: _Optional[str] = ...) -> None: ...
