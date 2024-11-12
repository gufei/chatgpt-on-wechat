import FriendAddNotice_pb2 as _FriendAddNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class FriendChangeNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "Friend")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    FRIEND_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    Friend: _FriendAddNotice_pb2.FriendMessage
    def __init__(self, WeChatId: _Optional[str] = ..., Friend: _Optional[_Union[_FriendAddNotice_pb2.FriendMessage, _Mapping]] = ...) -> None: ...
