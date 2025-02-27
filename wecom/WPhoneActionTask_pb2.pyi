"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumPhoneAction:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumPhoneActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumPhoneAction.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    Reboot: _EnumPhoneAction.ValueType  # 1
    """重启手机"""
    UploadLog: _EnumPhoneAction.ValueType  # 2
    """上传日志"""
    UploadFile: _EnumPhoneAction.ValueType  # 3
    """上传本地文件"""
    CleanAppCache: _EnumPhoneAction.ValueType  # 4
    """清除客服系统的图片缓存"""
    CleanWxCache: _EnumPhoneAction.ValueType  # 5
    """清除微信的图片视频缓存"""
    CleanFileUrlCache: _EnumPhoneAction.ValueType  # 6
    """清除手机缓存的文件url（用于防止重复上传）"""

class EnumPhoneAction(_EnumPhoneAction, metaclass=_EnumPhoneActionEnumTypeWrapper): ...

Reboot: EnumPhoneAction.ValueType  # 1
"""重启手机"""
UploadLog: EnumPhoneAction.ValueType  # 2
"""上传日志"""
UploadFile: EnumPhoneAction.ValueType  # 3
"""上传本地文件"""
CleanAppCache: EnumPhoneAction.ValueType  # 4
"""清除客服系统的图片缓存"""
CleanWxCache: EnumPhoneAction.ValueType  # 5
"""清除微信的图片视频缓存"""
CleanFileUrlCache: EnumPhoneAction.ValueType  # 6
"""清除手机缓存的文件url（用于防止重复上传）"""
global___EnumPhoneAction = EnumPhoneAction

@typing.final
class PhoneActionTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    IMEI_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    STRPARAM_FIELD_NUMBER: builtins.int
    INTPARAM_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    Imei: builtins.str
    """备用，用wxid或imei来定位手机"""
    Action: global___EnumPhoneAction.ValueType
    """指令"""
    StrParam: builtins.str
    """字符串参数，后续扩展用"""
    IntParam: builtins.int
    """整型参数，后续扩展用"""
    TaskId: builtins.int
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Imei: builtins.str = ...,
        Action: global___EnumPhoneAction.ValueType = ...,
        StrParam: builtins.str = ...,
        IntParam: builtins.int = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Action", b"Action", "Imei", b"Imei", "IntParam", b"IntParam", "StrParam", b"StrParam", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___PhoneActionTaskMessage = PhoneActionTaskMessage
