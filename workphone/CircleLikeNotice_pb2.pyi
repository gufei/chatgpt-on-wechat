from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CircleLikeNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "CircleId", "FriendId", "IsDelete", "PublishTime", "NickName")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CIRCLEID_FIELD_NUMBER: _ClassVar[int]
    FRIENDID_FIELD_NUMBER: _ClassVar[int]
    ISDELETE_FIELD_NUMBER: _ClassVar[int]
    PUBLISHTIME_FIELD_NUMBER: _ClassVar[int]
    NICKNAME_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    CircleId: int
    FriendId: str
    IsDelete: bool
    PublishTime: int
    NickName: str
    def __init__(self, WeChatId: _Optional[str] = ..., CircleId: _Optional[int] = ..., FriendId: _Optional[str] = ..., IsDelete: bool = ..., PublishTime: _Optional[int] = ..., NickName: _Optional[str] = ...) -> None: ...
