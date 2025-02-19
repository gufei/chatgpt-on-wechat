"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class OneWayCustomerPushNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    IDS_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    TaskId: builtins.int
    @property
    def Ids(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """单向好友RemoteId"""

    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Ids: collections.abc.Iterable[builtins.int] | None = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Ids", b"Ids", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___OneWayCustomerPushNoticeMessage = OneWayCustomerPushNoticeMessage
