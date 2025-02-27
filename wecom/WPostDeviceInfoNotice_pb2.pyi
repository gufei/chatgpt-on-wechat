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
class PostDeviceInfoNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    @typing.final
    class DeviceAppInfoMessage(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor

        PACKAGENAME_FIELD_NUMBER: builtins.int
        APPNAME_FIELD_NUMBER: builtins.int
        VERNUMBER_FIELD_NUMBER: builtins.int
        VERSION_FIELD_NUMBER: builtins.int
        PackageName: builtins.str
        AppName: builtins.str
        VerNumber: builtins.int
        Version: builtins.str
        def __init__(
            self,
            *,
            PackageName: builtins.str = ...,
            AppName: builtins.str = ...,
            VerNumber: builtins.int = ...,
            Version: builtins.str = ...,
        ) -> None: ...
        def ClearField(self, field_name: typing.Literal["AppName", b"AppName", "PackageName", b"PackageName", "VerNumber", b"VerNumber", "Version", b"Version"]) -> None: ...

    PHONEBRAND_FIELD_NUMBER: builtins.int
    PHONEMODEL_FIELD_NUMBER: builtins.int
    OSVERNUMBER_FIELD_NUMBER: builtins.int
    APPINFOS_FIELD_NUMBER: builtins.int
    NETTYPE_FIELD_NUMBER: builtins.int
    WXID_FIELD_NUMBER: builtins.int
    IMEI_FIELD_NUMBER: builtins.int
    IMSI1_FIELD_NUMBER: builtins.int
    IMSI2_FIELD_NUMBER: builtins.int
    NUMBER1_FIELD_NUMBER: builtins.int
    NUMBER2_FIELD_NUMBER: builtins.int
    ISHOOK_FIELD_NUMBER: builtins.int
    WXSUPPORT_FIELD_NUMBER: builtins.int
    PhoneBrand: builtins.str
    """手机品牌"""
    PhoneModel: builtins.str
    """手机型号"""
    OSVerNumber: builtins.int
    NetType: builtins.str
    WxId: builtins.int
    """微信id"""
    IMEI: builtins.str
    IMSI1: builtins.str
    """SIM卡1的IMSI"""
    IMSI2: builtins.str
    """SIM卡2的IMSI,"""
    Number1: builtins.str
    """SIM卡1的手机号，有可能读不到"""
    Number2: builtins.str
    """SIM卡2的手机好，有可能读不到"""
    IsHook: builtins.bool
    WxSupport: builtins.bool
    @property
    def AppInfos(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___PostDeviceInfoNoticeMessage.DeviceAppInfoMessage]:
        """App信息"""

    def __init__(
        self,
        *,
        PhoneBrand: builtins.str = ...,
        PhoneModel: builtins.str = ...,
        OSVerNumber: builtins.int = ...,
        AppInfos: collections.abc.Iterable[global___PostDeviceInfoNoticeMessage.DeviceAppInfoMessage] | None = ...,
        NetType: builtins.str = ...,
        WxId: builtins.int = ...,
        IMEI: builtins.str = ...,
        IMSI1: builtins.str = ...,
        IMSI2: builtins.str = ...,
        Number1: builtins.str = ...,
        Number2: builtins.str = ...,
        IsHook: builtins.bool = ...,
        WxSupport: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["AppInfos", b"AppInfos", "IMEI", b"IMEI", "IMSI1", b"IMSI1", "IMSI2", b"IMSI2", "IsHook", b"IsHook", "NetType", b"NetType", "Number1", b"Number1", "Number2", b"Number2", "OSVerNumber", b"OSVerNumber", "PhoneBrand", b"PhoneBrand", "PhoneModel", b"PhoneModel", "WxId", b"WxId", "WxSupport", b"WxSupport"]) -> None: ...

global___PostDeviceInfoNoticeMessage = PostDeviceInfoNoticeMessage
