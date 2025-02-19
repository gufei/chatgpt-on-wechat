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
class CustomerDelNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    REMOTEID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    RemoteId: builtins.int
    """被移除客户的remoteId"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        RemoteId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["RemoteId", b"RemoteId", "WxId", b"WxId"]) -> None: ...

global___CustomerDelNoticeMessage = CustomerDelNoticeMessage
