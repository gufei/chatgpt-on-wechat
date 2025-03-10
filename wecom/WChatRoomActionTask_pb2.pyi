"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
命名空间约定"""

import builtins
import collections.abc
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import sys
import typing

if sys.version_info >= (3, 10):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

class _EnumChatRoomAction:
    ValueType = typing.NewType("ValueType", builtins.int)
    V: typing_extensions.TypeAlias = ValueType

class _EnumChatRoomActionEnumTypeWrapper(google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[_EnumChatRoomAction.ValueType], builtins.type):
    DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor
    RoomName: _EnumChatRoomAction.ValueType  # 0
    """改群名 content=群名称"""
    ModifyPublicNoti: _EnumChatRoomAction.ValueType  # 1
    """改公告 content=公告内容"""
    AddMember: _EnumChatRoomAction.ValueType  # 2
    """拉人 Members不为空，content=附带消息"""
    KickMember: _EnumChatRoomAction.ValueType  # 3
    """踢人"""
    RoomShowName: _EnumChatRoomAction.ValueType  # 4
    """修改群内显示名 content=显示名 未实现"""
    AddToPhonebook: _EnumChatRoomAction.ValueType  # 5
    """未实现"""
    NoDisturb: _EnumChatRoomAction.ValueType  # 6
    """免打扰 IntValue=1 (消息免打扰 )，IntValue=0 取消,可设置单个联系人"""
    ExitRoom: _EnumChatRoomAction.ValueType  # 7
    """退群"""
    CreateRoom: _EnumChatRoomAction.ValueType  # 8
    """建群 Members不为空，content=群名称"""
    ViewAllMember: _EnumChatRoomAction.ValueType  # 9
    """查看所有群成员 未实现"""
    TransferOwner: _EnumChatRoomAction.ValueType  # 10
    """群主转让"""
    SetVerify: _EnumChatRoomAction.ValueType  # 11
    """未实现"""
    AddManager: _EnumChatRoomAction.ValueType  # 12
    """设置群管理员"""
    DelManager: _EnumChatRoomAction.ValueType  # 13
    """删除群管理员"""
    SetRemark: _EnumChatRoomAction.ValueType  # 14
    """未实现"""
    AddToFold: _EnumChatRoomAction.ValueType  # 15
    """折叠"""
    SetTop: _EnumChatRoomAction.ValueType  # 16
    """设置置顶 IntValue=0 取消置顶，IntValue=1 置顶,可设置单个联系人"""
    SetMarked: _EnumChatRoomAction.ValueType  # 17
    """标记 IntValue=0 取消标记，IntValue=1 标记,可设置单个联系人"""

class EnumChatRoomAction(_EnumChatRoomAction, metaclass=_EnumChatRoomActionEnumTypeWrapper): ...

RoomName: EnumChatRoomAction.ValueType  # 0
"""改群名 content=群名称"""
ModifyPublicNoti: EnumChatRoomAction.ValueType  # 1
"""改公告 content=公告内容"""
AddMember: EnumChatRoomAction.ValueType  # 2
"""拉人 Members不为空，content=附带消息"""
KickMember: EnumChatRoomAction.ValueType  # 3
"""踢人"""
RoomShowName: EnumChatRoomAction.ValueType  # 4
"""修改群内显示名 content=显示名 未实现"""
AddToPhonebook: EnumChatRoomAction.ValueType  # 5
"""未实现"""
NoDisturb: EnumChatRoomAction.ValueType  # 6
"""免打扰 IntValue=1 (消息免打扰 )，IntValue=0 取消,可设置单个联系人"""
ExitRoom: EnumChatRoomAction.ValueType  # 7
"""退群"""
CreateRoom: EnumChatRoomAction.ValueType  # 8
"""建群 Members不为空，content=群名称"""
ViewAllMember: EnumChatRoomAction.ValueType  # 9
"""查看所有群成员 未实现"""
TransferOwner: EnumChatRoomAction.ValueType  # 10
"""群主转让"""
SetVerify: EnumChatRoomAction.ValueType  # 11
"""未实现"""
AddManager: EnumChatRoomAction.ValueType  # 12
"""设置群管理员"""
DelManager: EnumChatRoomAction.ValueType  # 13
"""删除群管理员"""
SetRemark: EnumChatRoomAction.ValueType  # 14
"""未实现"""
AddToFold: EnumChatRoomAction.ValueType  # 15
"""折叠"""
SetTop: EnumChatRoomAction.ValueType  # 16
"""设置置顶 IntValue=0 取消置顶，IntValue=1 置顶,可设置单个联系人"""
SetMarked: EnumChatRoomAction.ValueType  # 17
"""标记 IntValue=0 取消标记，IntValue=1 标记,可设置单个联系人"""
global___EnumChatRoomAction = EnumChatRoomAction

@typing.final
class ChatRoomActionTaskMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    CONVID_FIELD_NUMBER: builtins.int
    ACTION_FIELD_NUMBER: builtins.int
    CONTENT_FIELD_NUMBER: builtins.int
    INTVALUE_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """商家所属微信号"""
    ConvId: builtins.int
    """会话remoteId"""
    Action: global___EnumChatRoomAction.ValueType
    """指令"""
    Content: builtins.str
    """指令内容"""
    IntValue: builtins.int
    """"""
    taskId: builtins.int
    @property
    def Members(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """操作的联系人（客户）"""

    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        ConvId: builtins.int = ...,
        Action: global___EnumChatRoomAction.ValueType = ...,
        Content: builtins.str = ...,
        IntValue: builtins.int = ...,
        Members: collections.abc.Iterable[builtins.int] | None = ...,
        taskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Action", b"Action", "Content", b"Content", "ConvId", b"ConvId", "IntValue", b"IntValue", "Members", b"Members", "WxId", b"WxId", "taskId", b"taskId"]) -> None: ...

global___ChatRoomActionTaskMessage = ChatRoomActionTaskMessage
