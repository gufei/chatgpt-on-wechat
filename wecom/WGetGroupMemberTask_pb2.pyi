"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import builtins
import google.protobuf.descriptor
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class GetGroupMemberTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    CONVID_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    ConvId: builtins.int
    """会话remoteid"""
    TaskId: builtins.int
    """任务id 在TaskResult中回传"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        ConvId: builtins.int = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ConvId", b"ConvId", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___GetGroupMemberTaskMessage = GetGroupMemberTaskMessage
