from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class RequestTalkDetailTaskMessage(_message.Message):
    __slots__ = ("MsgId", "WeChatId", "FriendId", "MsgSvrId", "Md5", "GetOriginal")
    MSGID_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    MSGSVRID_FIELD_NUMBER: _ClassVar[int]
    MD5_FIELD_NUMBER: _ClassVar[int]
    GETORIGINAL_FIELD_NUMBER: _ClassVar[int]
    MsgId: int
    WeChatId: str
    FriendId: str
    MsgSvrId: str
    Md5: str
    GetOriginal: bool
    def __init__(self, MsgId: _Optional[int] = ..., WeChatId: _Optional[str] = ..., FriendId: _Optional[str] = ..., MsgSvrId: _Optional[str] = ..., Md5: _Optional[str] = ..., GetOriginal: bool = ...) -> None: ...
