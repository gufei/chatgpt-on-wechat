import ChatRoomPushNotice_pb2 as _ChatRoomPushNotice_pb2
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class ChatRoomAddNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "ChatRoom")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    CHATROOM_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    ChatRoom: _ChatRoomPushNotice_pb2.ChatRoomMessage
    def __init__(self, WeChatId: _Optional[str] = ..., ChatRoom: _Optional[_Union[_ChatRoomPushNotice_pb2.ChatRoomMessage, _Mapping]] = ...) -> None: ...
