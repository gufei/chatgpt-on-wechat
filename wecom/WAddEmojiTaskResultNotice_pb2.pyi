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
class AddEmojiTaskResultNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    SUCCESS_FIELD_NUMBER: builtins.int
    ERRMSG_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    EMOJI_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """"""
    Success: builtins.bool
    """是否成功"""
    ErrMsg: builtins.str
    """错误内容描述 获取 成功时附带的结果内容"""
    TaskId: builtins.int
    Emoji: builtins.str
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Success: builtins.bool = ...,
        ErrMsg: builtins.str = ...,
        TaskId: builtins.int = ...,
        Emoji: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Emoji", b"Emoji", "ErrMsg", b"ErrMsg", "Success", b"Success", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___AddEmojiTaskResultNoticeMessage = AddEmojiTaskResultNoticeMessage
