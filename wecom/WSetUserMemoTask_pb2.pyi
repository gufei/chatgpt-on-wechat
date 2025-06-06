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
class SetUserMemoTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    REMOTEID_FIELD_NUMBER: builtins.int
    MEMO_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    RemoteId: builtins.int
    """联系人"""
    Memo: builtins.str
    """备注"""
    TaskId: builtins.int
    """任务id 在TaskResult中回传"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        RemoteId: builtins.int = ...,
        Memo: builtins.str = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Memo", b"Memo", "RemoteId", b"RemoteId", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___SetUserMemoTaskMessage = SetUserMemoTaskMessage
