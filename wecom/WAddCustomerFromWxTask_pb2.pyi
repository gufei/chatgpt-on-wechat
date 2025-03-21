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
class AddCustomerFromWxTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    INDEX_FIELD_NUMBER: builtins.int
    MSG_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """"""
    Count: builtins.int
    """添加的个数"""
    Index: builtins.int
    """添加的起始位置"""
    Msg: builtins.str
    """招呼语，缺省：你好这是我的企业微信，以后也可以在这里与我联系。"""
    TaskId: builtins.int
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Count: builtins.int = ...,
        Index: builtins.int = ...,
        Msg: builtins.str = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Count", b"Count", "Index", b"Index", "Msg", b"Msg", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___AddCustomerFromWxTaskMessage = AddCustomerFromWxTaskMessage
