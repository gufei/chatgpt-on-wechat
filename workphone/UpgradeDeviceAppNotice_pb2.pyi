from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class DeviceAppUpgradeMessage(_message.Message):
    __slots__ = ("VerNumber", "Version", "PackageName", "PackageUrl")
    VERNUMBER_FIELD_NUMBER: _ClassVar[int]
    VERSION_FIELD_NUMBER: _ClassVar[int]
    PACKAGENAME_FIELD_NUMBER: _ClassVar[int]
    PACKAGEURL_FIELD_NUMBER: _ClassVar[int]
    VerNumber: int
    Version: str
    PackageName: str
    PackageUrl: str
    def __init__(self, VerNumber: _Optional[int] = ..., Version: _Optional[str] = ..., PackageName: _Optional[str] = ..., PackageUrl: _Optional[str] = ...) -> None: ...

class UpgradeDeviceAppNoticeMessage(_message.Message):
    __slots__ = ("WeChatId", "IMEI", "AppInfos")
    WECHATID_FIELD_NUMBER: _ClassVar[int]
    IMEI_FIELD_NUMBER: _ClassVar[int]
    APPINFOS_FIELD_NUMBER: _ClassVar[int]
    WeChatId: str
    IMEI: str
    AppInfos: _containers.RepeatedCompositeFieldContainer[DeviceAppUpgradeMessage]
    def __init__(self, WeChatId: _Optional[str] = ..., IMEI: _Optional[str] = ..., AppInfos: _Optional[_Iterable[_Union[DeviceAppUpgradeMessage, _Mapping]]] = ...) -> None: ...
