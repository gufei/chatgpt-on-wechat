"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import WTransport_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class TalkMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    CONTENTTYPE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    ContentType: WTransport_pb2.EnumContentType.ValueType
    """消息类型 Text Picture Voice Video Link File NameCard WeApp Location"""
    Content: builtins.bytes
    """消息内容 文本，url（图片 视频 语音 文件），名片wxid，json(语音 文件 链接 小程序 位置)"""
    def __init__(
        self,
        *,
        ContentType: WTransport_pb2.EnumContentType.ValueType = ...,
        Content: builtins.bytes = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Content", b"Content", "ContentType", b"ContentType"]) -> None: ...

global___TalkMessage = TalkMessage

@typing.final
class QunFaTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    MSGS_FIELD_NUMBER: builtins.int
    CONVID_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    TaskId: builtins.int
    """"""
    @property
    def Msgs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___TalkMessage]: ...
    @property
    def ConvId(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """会话 RemoteId"""

    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Msgs: collections.abc.Iterable[global___TalkMessage] | None = ...,
        ConvId: collections.abc.Iterable[builtins.int] | None = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ConvId", b"ConvId", "Msgs", b"Msgs", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___QunFaTaskMessage = QunFaTaskMessage
