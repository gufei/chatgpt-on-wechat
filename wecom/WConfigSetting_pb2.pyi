"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import WConfigPushNotice_pb2
import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing.final
class ConfigSettingMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    BOOLCONFS_FIELD_NUMBER: builtins.int
    INTCONFS_FIELD_NUMBER: builtins.int
    STRCONFS_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """"""
    @property
    def BoolConfs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[WConfigPushNotice_pb2.BoolConfigMessage]: ...
    @property
    def IntConfs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[WConfigPushNotice_pb2.IntConfigMessage]: ...
    @property
    def StrConfs(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[WConfigPushNotice_pb2.StrConfigMessage]: ...
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        BoolConfs: collections.abc.Iterable[WConfigPushNotice_pb2.BoolConfigMessage] | None = ...,
        IntConfs: collections.abc.Iterable[WConfigPushNotice_pb2.IntConfigMessage] | None = ...,
        StrConfs: collections.abc.Iterable[WConfigPushNotice_pb2.StrConfigMessage] | None = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["BoolConfs", b"BoolConfs", "IntConfs", b"IntConfs", "StrConfs", b"StrConfs", "WxId", b"WxId"]) -> None: ...

global___ConfigSettingMessage = ConfigSettingMessage
