"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import WTransport_pb2
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class FriendTalkNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    CONVID_FIELD_NUMBER: builtins.int
    SENDERID_FIELD_NUMBER: builtins.int
    CONTENTTYPE_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    MSGID_FIELD_NUMBER: builtins.int
    MSGREMOTEID_FIELD_NUMBER: builtins.int
    CREATETIME_FIELD_NUMBER: builtins.int
    SENDERNAME_FIELD_NUMBER: builtins.int
    REFID_FIELD_NUMBER: builtins.int
    FLAG_FIELD_NUMBER: builtins.int
    ISREVOKE_FIELD_NUMBER: builtins.int
    ATME_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    CONVTYPE_FIELD_NUMBER: builtins.int
    CONVLOCALID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    ConvId: builtins.int
    """会话RemoteId"""
    SenderId: builtins.int
    """消息发送者Id"""
    ContentType: WTransport_pb2.EnumContentType.ValueType
    """发送的消息内容类型"""
    Content: builtins.bytes
    """内容 二进制流"""
    MsgId: builtins.int
    """服务端的主键id"""
    MsgRemoteId: builtins.int
    """消息唯一id"""
    CreateTime: builtins.int
    """消息时间"""
    SenderName: builtins.str
    """消息发送者名称"""
    RefId: builtins.int
    """引用消息的id"""
    Flag: builtins.int
    IsRevoke: builtins.bool
    AtMe: builtins.bool
    TaskId: builtins.int
    ConvType: builtins.int
    ConvLocalId: builtins.int
    """会话的LocalId"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        ConvId: builtins.int = ...,
        SenderId: builtins.int = ...,
        ContentType: WTransport_pb2.EnumContentType.ValueType = ...,
        Content: builtins.bytes = ...,
        MsgId: builtins.int = ...,
        MsgRemoteId: builtins.int = ...,
        CreateTime: builtins.int = ...,
        SenderName: builtins.str = ...,
        RefId: builtins.int = ...,
        Flag: builtins.int = ...,
        IsRevoke: builtins.bool = ...,
        AtMe: builtins.bool = ...,
        TaskId: builtins.int = ...,
        ConvType: builtins.int = ...,
        ConvLocalId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["AtMe", b"AtMe", "Content", b"Content", "ContentType", b"ContentType", "ConvId", b"ConvId", "ConvLocalId", b"ConvLocalId", "ConvType", b"ConvType", "CreateTime", b"CreateTime", "Flag", b"Flag", "IsRevoke", b"IsRevoke", "MsgId", b"MsgId", "MsgRemoteId", b"MsgRemoteId", "RefId", b"RefId", "SenderId", b"SenderId", "SenderName", b"SenderName", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___FriendTalkNoticeMessage = FriendTalkNoticeMessage
