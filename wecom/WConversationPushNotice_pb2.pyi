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
class ConversationPushNoticeMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    WXID_FIELD_NUMBER: builtins.int
    CONVERS_FIELD_NUMBER: builtins.int
    SIZE_FIELD_NUMBER: builtins.int
    COUNT_FIELD_NUMBER: builtins.int
    PAGE_FIELD_NUMBER: builtins.int
    ISEND_FIELD_NUMBER: builtins.int
    NEXTOFFSET_FIELD_NUMBER: builtins.int
    TOTAL_FIELD_NUMBER: builtins.int
    TASKID_FIELD_NUMBER: builtins.int
    WxId: builtins.int
    """设备企业WX号"""
    Size: builtins.int
    Count: builtins.int
    Page: builtins.int
    IsEnd: builtins.bool
    """本次推送是否结束"""
    NextOffset: builtins.int
    """"""
    Total: builtins.int
    """"""
    TaskId: builtins.int
    @property
    def Convers(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConversationMessage]:
        """好友信息模型 多个"""

    def __init__(
        self,
        *,
        WxId: builtins.int = ...,
        Convers: collections.abc.Iterable[global___ConversationMessage] | None = ...,
        Size: builtins.int = ...,
        Count: builtins.int = ...,
        Page: builtins.int = ...,
        IsEnd: builtins.bool = ...,
        NextOffset: builtins.int = ...,
        Total: builtins.int = ...,
        TaskId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Convers", b"Convers", "Count", b"Count", "IsEnd", b"IsEnd", "NextOffset", b"NextOffset", "Page", b"Page", "Size", b"Size", "TaskId", b"TaskId", "Total", b"Total", "WxId", b"WxId"]) -> None: ...

global___ConversationPushNoticeMessage = ConversationPushNoticeMessage

@typing.final
class ConversationMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    ID_FIELD_NUMBER: builtins.int
    REMOTEID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    TYPE_FIELD_NUMBER: builtins.int
    CREATOR_FIELD_NUMBER: builtins.int
    CREATETIME_FIELD_NUMBER: builtins.int
    UPDATETIME_FIELD_NUMBER: builtins.int
    NOTIFIED_FIELD_NUMBER: builtins.int
    FLAG_FIELD_NUMBER: builtins.int
    UNREADCNT_FIELD_NUMBER: builtins.int
    NOTICE_FIELD_NUMBER: builtins.int
    DIGEST_FIELD_NUMBER: builtins.int
    MEMBERS_FIELD_NUMBER: builtins.int
    ADMINS_FIELD_NUMBER: builtins.int
    HASEXTERNMEMBER_FIELD_NUMBER: builtins.int
    AVATARLIST_FIELD_NUMBER: builtins.int
    ISSAVED_FIELD_NUMBER: builtins.int
    ISMARKED_FIELD_NUMBER: builtins.int
    ISTOP_FIELD_NUMBER: builtins.int
    FWID_FIELD_NUMBER: builtins.int
    Id: builtins.int
    """"""
    RemoteId: builtins.int
    """单聊=联系人RemoteId, 群聊=公司id，部门id或其他"""
    Name: builtins.str
    Avatar: builtins.str
    Type: builtins.int
    """0 单聊 1 群聊"""
    Creator: builtins.int
    """创建者id"""
    CreateTime: builtins.int
    """创建时间"""
    UpdateTime: builtins.int
    """最后更新时间"""
    Notified: builtins.bool
    """是否新消息提示"""
    Flag: builtins.int
    """&2 全员群 &32 部门群"""
    UnreadCnt: builtins.int
    """未读消息数"""
    Notice: builtins.str
    """群公告"""
    Digest: builtins.str
    """最新消息概要"""
    HasExternMember: builtins.bool
    """是否有外部联系人（外部群）"""
    isSaved: builtins.bool
    """是否保存的群聊"""
    isMarked: builtins.bool
    """是否标注"""
    isTop: builtins.bool
    """是否置顶"""
    FwId: builtins.int
    """在线客服服务id"""
    @property
    def Members(self) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[global___ConvMemberMessage]:
        """群成员"""

    @property
    def Admins(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """群管理员"""

    @property
    def AvatarList(self) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.str]:
        """群聊头像列表，9宫格"""

    def __init__(
        self,
        *,
        Id: builtins.int = ...,
        RemoteId: builtins.int = ...,
        Name: builtins.str = ...,
        Avatar: builtins.str = ...,
        Type: builtins.int = ...,
        Creator: builtins.int = ...,
        CreateTime: builtins.int = ...,
        UpdateTime: builtins.int = ...,
        Notified: builtins.bool = ...,
        Flag: builtins.int = ...,
        UnreadCnt: builtins.int = ...,
        Notice: builtins.str = ...,
        Digest: builtins.str = ...,
        Members: collections.abc.Iterable[global___ConvMemberMessage] | None = ...,
        Admins: collections.abc.Iterable[builtins.int] | None = ...,
        HasExternMember: builtins.bool = ...,
        AvatarList: collections.abc.Iterable[builtins.str] | None = ...,
        isSaved: builtins.bool = ...,
        isMarked: builtins.bool = ...,
        isTop: builtins.bool = ...,
        FwId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Admins", b"Admins", "Avatar", b"Avatar", "AvatarList", b"AvatarList", "CreateTime", b"CreateTime", "Creator", b"Creator", "Digest", b"Digest", "Flag", b"Flag", "FwId", b"FwId", "HasExternMember", b"HasExternMember", "Id", b"Id", "Members", b"Members", "Name", b"Name", "Notice", b"Notice", "Notified", b"Notified", "RemoteId", b"RemoteId", "Type", b"Type", "UnreadCnt", b"UnreadCnt", "UpdateTime", b"UpdateTime", "isMarked", b"isMarked", "isSaved", b"isSaved", "isTop", b"isTop"]) -> None: ...

global___ConversationMessage = ConversationMessage

@typing.final
class ConvMemberMessage(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    REMOTEID_FIELD_NUMBER: builtins.int
    NAME_FIELD_NUMBER: builtins.int
    JOINTIME_FIELD_NUMBER: builtins.int
    JOINSCENE_FIELD_NUMBER: builtins.int
    AVATAR_FIELD_NUMBER: builtins.int
    CORPID_FIELD_NUMBER: builtins.int
    OPREMOTEID_FIELD_NUMBER: builtins.int
    RemoteId: builtins.int
    """群成员id"""
    Name: builtins.str
    """"""
    JoinTime: builtins.int
    JoinScene: builtins.int
    """加入场景，数值待确定"""
    Avatar: builtins.str
    """头像"""
    CorpId: builtins.int
    """公司id"""
    OpRemoteId: builtins.int
    """邀请人id"""
    def __init__(
        self,
        *,
        RemoteId: builtins.int = ...,
        Name: builtins.str = ...,
        JoinTime: builtins.int = ...,
        JoinScene: builtins.int = ...,
        Avatar: builtins.str = ...,
        CorpId: builtins.int = ...,
        OpRemoteId: builtins.int = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing.Literal["Avatar", b"Avatar", "CorpId", b"CorpId", "JoinScene", b"JoinScene", "JoinTime", b"JoinTime", "Name", b"Name", "OpRemoteId", b"OpRemoteId", "RemoteId", b"RemoteId"]) -> None: ...

global___ConvMemberMessage = ConvMemberMessage
