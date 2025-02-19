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
class TalkToFriendTaskResultNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    CODE_FIELD_NUMBER: builtins.int
    ERRMSG_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    CONVID_FIELD_NUMBER: builtins.int
    MSGID_FIELD_NUMBER: builtins.int
    MSGREMOTEID_FIELD_NUMBER: builtins.int
    CREATETIME_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    Success: builtins.bool
    """是否成功"""
    Code: WTransport_pb2.EnumErrorCode.ValueType
    """错误码 Success = true 忽略"""
    ErrMsg: builtins.str
    """错误内容描述 获取 成功时附带的结果内容"""
    TaskId: builtins.int
    """业务的id,通用的。"""
    ConvId: builtins.int
    """会话 RemoteId"""
    MsgId: builtins.int
    """消息id"""
    MsgRemoteId: builtins.int
    """消息RemoteId"""
    CreateTime: builtins.int
    """消息发送时间"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Success: builtins.bool = ...,
        Code: WTransport_pb2.EnumErrorCode.ValueType = ...,
        ErrMsg: builtins.str = ...,
        TaskId: builtins.int = ...,
        ConvId: builtins.int = ...,
        MsgId: builtins.int = ...,
        MsgRemoteId: builtins.int = ...,
        CreateTime: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Code", b"Code", "ConvId", b"ConvId", "CreateTime", b"CreateTime", "ErrMsg", b"ErrMsg", "MsgId", b"MsgId", "MsgRemoteId", b"MsgRemoteId", "Success", b"Success", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___TalkToFriendTaskResultNoticeMessage = TalkToFriendTaskResultNoticeMessage
