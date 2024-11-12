import TransportMessage_pb2 as _TransportMessage_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class TalkToFriendTaskResultNoticeMessage(_message.Message):
    __slots__ = ("Success", "Code", "ErrMsg", "WeChatId", "FriendId", "MsgId", "MsgSvrId", "CreateTime")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    CODE_FIELD_NUMBER: _ClassVar[int]
    ERRMSG_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MSGID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    CREATETIME_FIELD_NUMBER: _ClassVar[int]
    Success: bool
    Code: _TransportMessage_pb2.EnumErrorCode
    ErrMsg: str
    WeChatId: str
    FriendId: str
    MsgId: int
    MsgSvrId: int
    CreateTime: int
    def __init__(self, Success: bool = ..., Code: _Optional[_Union[_TransportMessage_pb2.EnumErrorCode, str]] = ..., ErrMsg: _Optional[str] = ..., WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., MsgId: _Optional[int] = ..., MsgSvrId: _Optional[int] = ..., CreateTime: _Optional[int] = ...) -> None: ...
