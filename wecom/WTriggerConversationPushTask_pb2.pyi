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
class TriggerConversationPushTaskMessage(google.protobuf.message.Message):
    """定义消息类型 TriggerConversationPushTask"""

    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    WxId: builtins.str
    def __init__(
        self,
        *,
        WxId: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["WxId", b"WxId"]) -> None: ...

global___TriggerConversationPushTaskMessage = TriggerConversationPushTaskMessage
