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
class PullMyQrCodeTaskResultNoticeMessage(google.protobuf.message.Message):
    """通用Trigger任务消息"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERRMSG_FIELD_NUMBER: builtins.int
    URL_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """"""
    Success: builtins.bool
    """是否成功"""
    ErrMsg: builtins.str
    """错误内容描述 获取 成功时附带的结果内容"""
    Url: builtins.str
    """"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Success: builtins.bool = ...,
        ErrMsg: builtins.str = ...,
        Url: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["ErrMsg", b"ErrMsg", "Success", b"Success", "Url", b"Url", "WxId", b"WxId"]) -> None: ...

global___PullMyQrCodeTaskResultNoticeMessage = PullMyQrCodeTaskResultNoticeMessage
