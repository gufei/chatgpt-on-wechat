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
class DownloadFileByMsgIdTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    MSGID_FIELD_NUMBER: builtins.int
    MSGREMOTEID_FIELD_NUMBER: builtins.int
    FILETYPE_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    RESEND_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """"""
    MsgId: builtins.int
    MsgRemoteId: builtins.int
    """"""
    FileType: builtins.int
    """下载文件的类型 0 原始文件（原图，视频，音频，文件）"""
    TaskId: builtins.int
    ReSend: builtins.bool
    """重新上传文件"""
    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        MsgId: builtins.int = ...,
        MsgRemoteId: builtins.int = ...,
        FileType: builtins.int = ...,
        TaskId: builtins.int = ...,
        ReSend: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["FileType", b"FileType", "MsgId", b"MsgId", "MsgRemoteId", b"MsgRemoteId", "ReSend", b"ReSend", "TaskId", b"TaskId", "WxId", b"WxId"]) -> None: ...

global___DownloadFileByMsgIdTaskMessage = DownloadFileByMsgIdTaskMessage
