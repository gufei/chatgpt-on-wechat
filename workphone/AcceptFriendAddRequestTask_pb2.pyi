from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class AcceptFriendAddRequestTaskMessage(_message.Message):
    __slots__ = ("WeChatId", "FriendId", "AddWithWW", "Operation", "Remark", "FriendNick", "ReplyMsg", "TaskId", "OnlyWW")
    class EnumFriendAddOperation(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = ()
        Ignore: _ClassVar[AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation]
        Accept: _ClassVar[AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation]
        Reject: _ClassVar[AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation]
    Ignore: AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation
    Accept: AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation
    Reject: AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    ADDWITHWW_FIELD_NUMBER: _ClassVar[int]
    OPERATION_FIELD_NUMBER: _ClassVar[int]
    REMARK_FIELD_NUMBER: _ClassVar[int]
    FRIENDNICK_FIELD_NUMBER: _ClassVar[int]
    REPLYMSG_FIELD_NUMBER: _ClassVar[int]
    TASKID_FIELD_NUMBER: _ClassVar[int]
    ONLYWW_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    FriendId: str
    AddWithWW: bool
    Operation: AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation
    Remark: str
    FriendNick: str
    ReplyMsg: str
    TaskId: int
    OnlyWW: bool
    def __init__(self, WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., AddWithWW: bool = ..., Operation: _Optional[_Union[AcceptFriendAddRequestTaskMessage.EnumFriendAddOperation, str]] = ..., Remark: _Optional[str] = ..., FriendNick: _Optional[str] = ..., ReplyMsg: _Optional[str] = ..., TaskId: _Optional[int] = ..., OnlyWW: bool = ...) -> None: ...
