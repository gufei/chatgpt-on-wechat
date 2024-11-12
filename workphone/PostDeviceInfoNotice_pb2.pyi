from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class PostDeviceInfoNoticeMessage(_message.Message):
    __slots__ = ("PhoneBrand", "PhoneModel", "OSVerNumber", "AppInfos", "NetType", "WeChatId", "IMEI", "IMSI1", "IMSI2", "Number1", "Number2", "IsHook", "WxSupport")
    class DeviceAppInfoMessage(_message.Message):
        __slots__ = ("PackageName", "AppName", "VerNumber", "Version")
        PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
        APPNAME_FIELD_NUMBER: _ClassVar[int]
        VERNUMBER_FIELD_NUMBER: _ClassVar[int]
        VERSION_FIELD_NUMBER: _ClassVar[int]
        PackageName: str
        AppName: str
        VerNumber: int
        Version: str
        def __init__(self, PackageName: _Optional[str] = ..., AppName: _Optional[str] = ..., VerNumber: _Optional[int] = ..., Version: _Optional[str] = ...) -> None: ...
    PHONEBRAND_FIELD_NUMBER: _ClassVar[int]
    PHONEMODEL_FIELD_NUMBER: _ClassVar[int]
    OSVERNUMBER_FIELD_NUMBER: _ClassVar[int]
    APPINFOS_FIELD_NUMBER: _ClassVar[int]
    NETTYPE_FIELD_NUMBER: _ClassVar[int]
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    IMSI1_FIELD_NUMBER: _ClassVar[int]
    IMSI2_FIELD_NUMBER: _ClassVar[int]
    NUMBER1_FIELD_NUMBER: _ClassVar[int]
    NUMBER2_FIELD_NUMBER: _ClassVar[int]
    ISHOOK_FIELD_NUMBER: _ClassVar[int]
    WXSUPPORT_FIELD_NUMBER: _ClassVar[int]
    PhoneBrand: str
    PhoneModel: str
    OSVerNumber: int
    AppInfos: _containers.RepeatedCompositeFieldContainer[PostDeviceInfoNoticeMessage.DeviceAppInfoMessage]
    NetType: str
    WeChatId: str
    IMEI: str
    IMSI1: str
    IMSI2: str
    Number1: str
    Number2: str
    IsHook: bool
    WxSupport: bool
    def __init__(self, PhoneBrand: _Optional[str] = ..., PhoneModel: _Optional[str] = ..., OSVerNumber: _Optional[int] = ..., AppInfos: _Optional[_Iterable[_Union[PostDeviceInfoNoticeMessage.DeviceAppInfoMessage, _Mapping]]] = ..., NetType: _Optional[str] = ..., WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., IMSI1: _Optional[str] = ..., IMSI2: _Optional[str] = ..., Number1: _Optional[str] = ..., Number2: _Optional[str] = ..., IsHook: bool = ..., WxSupport: bool = ...) -> None: ...
