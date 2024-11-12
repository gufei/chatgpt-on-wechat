from google.protobuf import any_pb2 as _any_pb2
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class EnumMsgType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownMsg: _ClassVar[EnumMsgType]
    HeartBeatReq: _ClassVar[EnumMsgType]
    MsgReceivedAck: _ClassVar[EnumMsgType]
    Error: _ClassVar[EnumMsgType]
    DeviceAuthReq: _ClassVar[EnumMsgType]
    DeviceAuthRsp: _ClassVar[EnumMsgType]
    DeviceExitNotice: _ClassVar[EnumMsgType]
    AccountForceOfflineNotice: _ClassVar[EnumMsgType]
    RedirectNotice: _ClassVar[EnumMsgType]
    TriggerDeviceInfo: _ClassVar[EnumMsgType]
    TriggerWechatPushTask: _ClassVar[EnumMsgType]
    WeChatOnlineNotice: _ClassVar[EnumMsgType]
    WeChatOfflineNotice: _ClassVar[EnumMsgType]
    FriendAddNotice: _ClassVar[EnumMsgType]
    FriendDelNotice: _ClassVar[EnumMsgType]
    FriendTalkNotice: _ClassVar[EnumMsgType]
    TaskResultNotice: _ClassVar[EnumMsgType]
    WeChatTalkToFriendNotice: _ClassVar[EnumMsgType]
    FriendAddReqeustNotice: _ClassVar[EnumMsgType]
    TalkToFriendTaskResultNotice: _ClassVar[EnumMsgType]
    RequestTalkDetailTaskResultNotice: _ClassVar[EnumMsgType]
    PullWeChatQrCodeTaskResultNotice: _ClassVar[EnumMsgType]
    CircleNewPublishNotice: _ClassVar[EnumMsgType]
    CircleDelNotice: _ClassVar[EnumMsgType]
    CircleLikeNotice: _ClassVar[EnumMsgType]
    CircleCommentNotice: _ClassVar[EnumMsgType]
    PostMessageReadNotice: _ClassVar[EnumMsgType]
    ChatRoomAddNotice: _ClassVar[EnumMsgType]
    ContactLabelAddNotice: _ClassVar[EnumMsgType]
    TakeMoneyTaskResultNotice: _ClassVar[EnumMsgType]
    CircleDetailNotice: _ClassVar[EnumMsgType]
    ChatRoomDelNotice: _ClassVar[EnumMsgType]
    ChatRoomChangedNotice: _ClassVar[EnumMsgType]
    PullChatRoomQrCodeTaskResultNotice: _ClassVar[EnumMsgType]
    ContactLabelDelNotice: _ClassVar[EnumMsgType]
    ChatMsgIdsPushNotice: _ClassVar[EnumMsgType]
    ChatMsgFilePushNotice: _ClassVar[EnumMsgType]
    FriendChangeNotice: _ClassVar[EnumMsgType]
    PhoneStateWarningNotice: _ClassVar[EnumMsgType]
    MsgDelNotice: _ClassVar[EnumMsgType]
    ConvDelNotice: _ClassVar[EnumMsgType]
    TalkToFriendTask: _ClassVar[EnumMsgType]
    PostSNSNewsTask: _ClassVar[EnumMsgType]
    AddFriendsTask: _ClassVar[EnumMsgType]
    PostSNSNewsTaskResultNotice: _ClassVar[EnumMsgType]
    DeleteSNSNewsTask: _ClassVar[EnumMsgType]
    AcceptFriendAddRequestTask: _ClassVar[EnumMsgType]
    WeChatGroupSendTask: _ClassVar[EnumMsgType]
    RequestTalkDetailTask: _ClassVar[EnumMsgType]
    PullWeChatQrCodeTask: _ClassVar[EnumMsgType]
    TriggerFriendPushTask: _ClassVar[EnumMsgType]
    TriggerCirclePushTask: _ClassVar[EnumMsgType]
    CircleCommentDeleteTask: _ClassVar[EnumMsgType]
    CircleCommentDeleteTaskResultNotice: _ClassVar[EnumMsgType]
    CircleCommentReplyTask: _ClassVar[EnumMsgType]
    CircleCommentReplyTaskResultNotice: _ClassVar[EnumMsgType]
    TriggerMessageReadTask: _ClassVar[EnumMsgType]
    RevokeMessageTask: _ClassVar[EnumMsgType]
    ForwardMessageTask: _ClassVar[EnumMsgType]
    TriggerHistoryMsgPushTask: _ClassVar[EnumMsgType]
    PullChatRoomQrCodeTask: _ClassVar[EnumMsgType]
    SendMultiPictureTask: _ClassVar[EnumMsgType]
    ForwardMultiMessageTask: _ClassVar[EnumMsgType]
    UpgradeAppNotice: _ClassVar[EnumMsgType]
    UpgradeDeviceAppNotice: _ClassVar[EnumMsgType]
    PostFriendDetectTask: _ClassVar[EnumMsgType]
    PostStopFriendDetectTask: _ClassVar[EnumMsgType]
    PostDeleteDeviceNotice: _ClassVar[EnumMsgType]
    OneKeyLikeTask: _ClassVar[EnumMsgType]
    ModifyFriendMemoTask: _ClassVar[EnumMsgType]
    AddFriendWithSceneTask: _ClassVar[EnumMsgType]
    TakeLuckyMoneyTask: _ClassVar[EnumMsgType]
    PullFriendCircleTask: _ClassVar[EnumMsgType]
    PullCircleDetailTask: _ClassVar[EnumMsgType]
    CircleLikeTask: _ClassVar[EnumMsgType]
    TriggerChatroomPushTask: _ClassVar[EnumMsgType]
    RequestChatRoomInfoTask: _ClassVar[EnumMsgType]
    RequestContactsInfoTask: _ClassVar[EnumMsgType]
    ChatRoomActionTask: _ClassVar[EnumMsgType]
    AddFriendInChatRoomTask: _ClassVar[EnumMsgType]
    AddFriendFromPhonebookTask: _ClassVar[EnumMsgType]
    DeleteFriendTask: _ClassVar[EnumMsgType]
    SendLuckyMoneyTask: _ClassVar[EnumMsgType]
    RequestTalkContentTask: _ClassVar[EnumMsgType]
    RequestTalkContentTaskResultNotice: _ClassVar[EnumMsgType]
    ForwardMessageByContentTask: _ClassVar[EnumMsgType]
    ChatRoomInviteApproveTask: _ClassVar[EnumMsgType]
    WechatLogoutTask: _ClassVar[EnumMsgType]
    PhoneActionTask: _ClassVar[EnumMsgType]
    ContactLabelTask: _ClassVar[EnumMsgType]
    ContactLabelDeleteTask: _ClassVar[EnumMsgType]
    VoiceTransTextTask: _ClassVar[EnumMsgType]
    FindContactTask: _ClassVar[EnumMsgType]
    FindContactTaskResult: _ClassVar[EnumMsgType]
    AgreeJoinChatRoomTask: _ClassVar[EnumMsgType]
    ClearAllChatMsgTask: _ClassVar[EnumMsgType]
    SendFriendVerifyTask: _ClassVar[EnumMsgType]
    TriggerConversationPushTask: _ClassVar[EnumMsgType]
    WechatSettingTask: _ClassVar[EnumMsgType]
    PullFriendAddReqListTask: _ClassVar[EnumMsgType]
    TriggerBizContactPushTask: _ClassVar[EnumMsgType]
    AddFriendNameCardTask: _ClassVar[EnumMsgType]
    TriggerChatMsgIdsPushTask: _ClassVar[EnumMsgType]
    RequestTalkMsgTask: _ClassVar[EnumMsgType]
    RequestTalkMsgTaskResultNotice: _ClassVar[EnumMsgType]
    SearchBizContactTask: _ClassVar[EnumMsgType]
    SearchBizContactTaskResultNotice: _ClassVar[EnumMsgType]
    PhoneStateTask: _ClassVar[EnumMsgType]
    PhoneStateTaskResultNotice: _ClassVar[EnumMsgType]
    WeChatLocationTask: _ClassVar[EnumMsgType]
    WeChatLocationTaskResultNotice: _ClassVar[EnumMsgType]
    RemittanceTask: _ClassVar[EnumMsgType]
    WalletBalanceTask: _ClassVar[EnumMsgType]
    WalletBalanceTaskResultNotice: _ClassVar[EnumMsgType]
    AddFriendNotice: _ClassVar[EnumMsgType]
    QueryHbDetailTask: _ClassVar[EnumMsgType]
    QueryHbDetailTaskResultNotice: _ClassVar[EnumMsgType]
    JoinGroupByQrTask: _ClassVar[EnumMsgType]
    SendJielongTask: _ClassVar[EnumMsgType]
    CDNDownloadFileTask: _ClassVar[EnumMsgType]
    ContactSetLabelTask: _ClassVar[EnumMsgType]
    CDNDownloadResultNotice: _ClassVar[EnumMsgType]
    PullEmojiInfoTask: _ClassVar[EnumMsgType]
    PullEmojiInfoTaskResultNotice: _ClassVar[EnumMsgType]
    TriggerCircleMsgPushTask: _ClassVar[EnumMsgType]
    CircleMsgReadTask: _ClassVar[EnumMsgType]
    CircleMsgClearTask: _ClassVar[EnumMsgType]
    GetContactInfoTask: _ClassVar[EnumMsgType]
    ContactInfoNotice: _ClassVar[EnumMsgType]
    GetFriendDetectResult: _ClassVar[EnumMsgType]
    FriendDetectResultNotice: _ClassVar[EnumMsgType]
    TriggerUnReadTask: _ClassVar[EnumMsgType]
    ScreenShotTask: _ClassVar[EnumMsgType]
    ScreenShotTaskResultNotice: _ClassVar[EnumMsgType]
    GetA8KeyTask: _ClassVar[EnumMsgType]
    TriggerQwUserPush: _ClassVar[EnumMsgType]
    QwUserPUshNotice: _ClassVar[EnumMsgType]
    QueryHbStatusTask: _ClassVar[EnumMsgType]
    QueryHbStatusTaskResultNotice: _ClassVar[EnumMsgType]
    SendSmsTask: _ClassVar[EnumMsgType]
    CallLogPushNotice: _ClassVar[EnumMsgType]
    SmsPushNotice: _ClassVar[EnumMsgType]
    SmsReadNotice: _ClassVar[EnumMsgType]
    SmsSentNotice: _ClassVar[EnumMsgType]
    PullSmsTask: _ClassVar[EnumMsgType]
    PullSmsTaskResultNotice: _ClassVar[EnumMsgType]
    PullCallLogTask: _ClassVar[EnumMsgType]
    PullCallLogTaskResultNotice: _ClassVar[EnumMsgType]
    TriggerConfigPush: _ClassVar[EnumMsgType]
    ConfigPushNotice: _ClassVar[EnumMsgType]
    SetConfigTask: _ClassVar[EnumMsgType]
    FriendPushNotice: _ClassVar[EnumMsgType]
    PostDeviceInfoNotice: _ClassVar[EnumMsgType]
    PostFriendDetectCountNotice: _ClassVar[EnumMsgType]
    CirclePushNotice: _ClassVar[EnumMsgType]
    OneKeyLikeTaskResultNotice: _ClassVar[EnumMsgType]
    ChatroomPushNotice: _ClassVar[EnumMsgType]
    ContactLabelInfoNotice: _ClassVar[EnumMsgType]
    HistoryMsgPushNotice: _ClassVar[EnumMsgType]
    ChatRoomMembersNotice: _ClassVar[EnumMsgType]
    ConversationPushNotice: _ClassVar[EnumMsgType]
    FriendAddReqListNotice: _ClassVar[EnumMsgType]
    BizContactPushNotice: _ClassVar[EnumMsgType]
    BizContactAddNotice: _ClassVar[EnumMsgType]
    CircleMsgPushNotice: _ClassVar[EnumMsgType]
    QwConversPushNotice: _ClassVar[EnumMsgType]
    BizConversPushNotice: _ClassVar[EnumMsgType]
    GetWeChatsReq: _ClassVar[EnumMsgType]
    GetWeChatsRsp: _ClassVar[EnumMsgType]
    RecentFriendChangeNotice: _ClassVar[EnumMsgType]
    TodayFriendChangeNotice: _ClassVar[EnumMsgType]
    AccountLogoutNotice: _ClassVar[EnumMsgType]
    WeChatLoginNotice: _ClassVar[EnumMsgType]
    SyncFriendListAsyncReq: _ClassVar[EnumMsgType]
    SyncFriendListAsyncRsp: _ClassVar[EnumMsgType]
    SyncRecentFriendListAsyncReq: _ClassVar[EnumMsgType]
    SyncRecentFriendListAsyncRsp: _ClassVar[EnumMsgType]
    SyncTodayFriendListAsyncReq: _ClassVar[EnumMsgType]
    SyncTodayFriendListAsyncRsp: _ClassVar[EnumMsgType]
    SyncFriendMessageAsyncReq: _ClassVar[EnumMsgType]
    SyncFriendMessageAsyncRsp: _ClassVar[EnumMsgType]
    TalkToFriendTaskReceived: _ClassVar[EnumMsgType]
    ReadChatMessageNotice: _ClassVar[EnumMsgType]
    SyncFriendAddReqeustAsyncReq: _ClassVar[EnumMsgType]
    SyncFriendAddRequestAsyncRsp: _ClassVar[EnumMsgType]
    WeChatForceOfflineNotice: _ClassVar[EnumMsgType]
    SyncQuickReplyAsyncReq: _ClassVar[EnumMsgType]
    SyncQuickReplyAsyncRsp: _ClassVar[EnumMsgType]
    QuickReplyAddNotice: _ClassVar[EnumMsgType]
    QuickReplyAddReceived: _ClassVar[EnumMsgType]
    QuickReplyDelNotice: _ClassVar[EnumMsgType]
    GetTagGroupReq: _ClassVar[EnumMsgType]
    GetTagGroupRsp: _ClassVar[EnumMsgType]
    GetTagFriendsReq: _ClassVar[EnumMsgType]
    GetTagFriendsRsp: _ClassVar[EnumMsgType]
    WeChatForceOnlineNotice: _ClassVar[EnumMsgType]
    DeleteRecentFriendNotice: _ClassVar[EnumMsgType]
    DeleteTodayFriendNotice: _ClassVar[EnumMsgType]
    WeChatInfoChangeNotice: _ClassVar[EnumMsgType]
    GetLastestVersionReq: _ClassVar[EnumMsgType]
    GetLastestVersionRsp: _ClassVar[EnumMsgType]
    CheckDeviceAppVersionReq: _ClassVar[EnumMsgType]
    CheckDeviceAppVersionRsp: _ClassVar[EnumMsgType]
    NewAppVersionPublishNotice: _ClassVar[EnumMsgType]
    WeChatLoginNoticeResp: _ClassVar[EnumMsgType]
    GroupMemberAddProgress: _ClassVar[EnumMsgType]
    PostAppInfoReq: _ClassVar[EnumMsgType]
    PostLogReq: _ClassVar[EnumMsgType]

class EnumErrorCode(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    Success: _ClassVar[EnumErrorCode]
    NoRight: _ClassVar[EnumErrorCode]
    InvalidParam: _ClassVar[EnumErrorCode]
    InternalError: _ClassVar[EnumErrorCode]
    TargetNotOnline: _ClassVar[EnumErrorCode]

class EnumGender(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownGender: _ClassVar[EnumGender]
    Male: _ClassVar[EnumGender]
    Female: _ClassVar[EnumGender]

class EnumContentType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownContent: _ClassVar[EnumContentType]
    Text: _ClassVar[EnumContentType]
    Picture: _ClassVar[EnumContentType]
    Voice: _ClassVar[EnumContentType]
    Video: _ClassVar[EnumContentType]
    System: _ClassVar[EnumContentType]
    Link: _ClassVar[EnumContentType]
    LinkExt: _ClassVar[EnumContentType]
    File: _ClassVar[EnumContentType]
    NameCard: _ClassVar[EnumContentType]
    Location: _ClassVar[EnumContentType]
    LuckyMoney: _ClassVar[EnumContentType]
    MoneyTrans: _ClassVar[EnumContentType]
    WeApp: _ClassVar[EnumContentType]
    Emoji: _ClassVar[EnumContentType]
    RoomManage: _ClassVar[EnumContentType]
    Sys_LuckyMoney: _ClassVar[EnumContentType]
    RoomSystem: _ClassVar[EnumContentType]
    BizLink: _ClassVar[EnumContentType]
    AudioCall: _ClassVar[EnumContentType]
    VideoCall: _ClassVar[EnumContentType]
    NotifyMsg: _ClassVar[EnumContentType]
    QuoteMsg: _ClassVar[EnumContentType]
    JieLongMsg: _ClassVar[EnumContentType]
    ShiPinHao: _ClassVar[EnumContentType]
    RoomLiving: _ClassVar[EnumContentType]
    PaiYiPai: _ClassVar[EnumContentType]
    FinderLive: _ClassVar[EnumContentType]
    KefuNameCard: _ClassVar[EnumContentType]
    QiyeNameCard: _ClassVar[EnumContentType]
    UnSupport: _ClassVar[EnumContentType]

class EnumOnlineState(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownState: _ClassVar[EnumOnlineState]
    Online: _ClassVar[EnumOnlineState]
    Offline: _ClassVar[EnumOnlineState]

class EnumTaskType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownTask: _ClassVar[EnumTaskType]
    ReadTencentNews: _ClassVar[EnumTaskType]
    ReadMPArticles: _ClassVar[EnumTaskType]
    ReadKYKArticles: _ClassVar[EnumTaskType]

class EnumAccountType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    UnknownAccountType: _ClassVar[EnumAccountType]
    Main: _ClassVar[EnumAccountType]
    SubUser: _ClassVar[EnumAccountType]

class EnumSendStatus(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NoAction: _ClassVar[EnumSendStatus]
    Sending: _ClassVar[EnumSendStatus]
    SendSuccess: _ClassVar[EnumSendStatus]
    SendError: _ClassVar[EnumSendStatus]

class EnumForceOfflineReason(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = ()
    NoReason: _ClassVar[EnumForceOfflineReason]
    FuckedByOtherAuthorizer: _ClassVar[EnumForceOfflineReason]
    ByReAlloc: _ClassVar[EnumForceOfflineReason]
    ByDeviceOffline: _ClassVar[EnumForceOfflineReason]
    ByWeChatOffline: _ClassVar[EnumForceOfflineReason]
UnknownMsg: EnumMsgType
HeartBeatReq: EnumMsgType
MsgReceivedAck: EnumMsgType
Error: EnumMsgType
DeviceAuthReq: EnumMsgType
DeviceAuthRsp: EnumMsgType
DeviceExitNotice: EnumMsgType
AccountForceOfflineNotice: EnumMsgType
RedirectNotice: EnumMsgType
TriggerDeviceInfo: EnumMsgType
TriggerWechatPushTask: EnumMsgType
WeChatOnlineNotice: EnumMsgType
WeChatOfflineNotice: EnumMsgType
FriendAddNotice: EnumMsgType
FriendDelNotice: EnumMsgType
FriendTalkNotice: EnumMsgType
TaskResultNotice: EnumMsgType
WeChatTalkToFriendNotice: EnumMsgType
FriendAddReqeustNotice: EnumMsgType
TalkToFriendTaskResultNotice: EnumMsgType
RequestTalkDetailTaskResultNotice: EnumMsgType
PullWeChatQrCodeTaskResultNotice: EnumMsgType
CircleNewPublishNotice: EnumMsgType
CircleDelNotice: EnumMsgType
CircleLikeNotice: EnumMsgType
CircleCommentNotice: EnumMsgType
PostMessageReadNotice: EnumMsgType
ChatRoomAddNotice: EnumMsgType
ContactLabelAddNotice: EnumMsgType
TakeMoneyTaskResultNotice: EnumMsgType
CircleDetailNotice: EnumMsgType
ChatRoomDelNotice: EnumMsgType
ChatRoomChangedNotice: EnumMsgType
PullChatRoomQrCodeTaskResultNotice: EnumMsgType
ContactLabelDelNotice: EnumMsgType
ChatMsgIdsPushNotice: EnumMsgType
ChatMsgFilePushNotice: EnumMsgType
FriendChangeNotice: EnumMsgType
PhoneStateWarningNotice: EnumMsgType
MsgDelNotice: EnumMsgType
ConvDelNotice: EnumMsgType
TalkToFriendTask: EnumMsgType
PostSNSNewsTask: EnumMsgType
AddFriendsTask: EnumMsgType
PostSNSNewsTaskResultNotice: EnumMsgType
DeleteSNSNewsTask: EnumMsgType
AcceptFriendAddRequestTask: EnumMsgType
WeChatGroupSendTask: EnumMsgType
RequestTalkDetailTask: EnumMsgType
PullWeChatQrCodeTask: EnumMsgType
TriggerFriendPushTask: EnumMsgType
TriggerCirclePushTask: EnumMsgType
CircleCommentDeleteTask: EnumMsgType
CircleCommentDeleteTaskResultNotice: EnumMsgType
CircleCommentReplyTask: EnumMsgType
CircleCommentReplyTaskResultNotice: EnumMsgType
TriggerMessageReadTask: EnumMsgType
RevokeMessageTask: EnumMsgType
ForwardMessageTask: EnumMsgType
TriggerHistoryMsgPushTask: EnumMsgType
PullChatRoomQrCodeTask: EnumMsgType
SendMultiPictureTask: EnumMsgType
ForwardMultiMessageTask: EnumMsgType
UpgradeAppNotice: EnumMsgType
UpgradeDeviceAppNotice: EnumMsgType
PostFriendDetectTask: EnumMsgType
PostStopFriendDetectTask: EnumMsgType
PostDeleteDeviceNotice: EnumMsgType
OneKeyLikeTask: EnumMsgType
ModifyFriendMemoTask: EnumMsgType
AddFriendWithSceneTask: EnumMsgType
TakeLuckyMoneyTask: EnumMsgType
PullFriendCircleTask: EnumMsgType
PullCircleDetailTask: EnumMsgType
CircleLikeTask: EnumMsgType
TriggerChatroomPushTask: EnumMsgType
RequestChatRoomInfoTask: EnumMsgType
RequestContactsInfoTask: EnumMsgType
ChatRoomActionTask: EnumMsgType
AddFriendInChatRoomTask: EnumMsgType
AddFriendFromPhonebookTask: EnumMsgType
DeleteFriendTask: EnumMsgType
SendLuckyMoneyTask: EnumMsgType
RequestTalkContentTask: EnumMsgType
RequestTalkContentTaskResultNotice: EnumMsgType
ForwardMessageByContentTask: EnumMsgType
ChatRoomInviteApproveTask: EnumMsgType
WechatLogoutTask: EnumMsgType
PhoneActionTask: EnumMsgType
ContactLabelTask: EnumMsgType
ContactLabelDeleteTask: EnumMsgType
VoiceTransTextTask: EnumMsgType
FindContactTask: EnumMsgType
FindContactTaskResult: EnumMsgType
AgreeJoinChatRoomTask: EnumMsgType
ClearAllChatMsgTask: EnumMsgType
SendFriendVerifyTask: EnumMsgType
TriggerConversationPushTask: EnumMsgType
WechatSettingTask: EnumMsgType
PullFriendAddReqListTask: EnumMsgType
TriggerBizContactPushTask: EnumMsgType
AddFriendNameCardTask: EnumMsgType
TriggerChatMsgIdsPushTask: EnumMsgType
RequestTalkMsgTask: EnumMsgType
RequestTalkMsgTaskResultNotice: EnumMsgType
SearchBizContactTask: EnumMsgType
SearchBizContactTaskResultNotice: EnumMsgType
PhoneStateTask: EnumMsgType
PhoneStateTaskResultNotice: EnumMsgType
WeChatLocationTask: EnumMsgType
WeChatLocationTaskResultNotice: EnumMsgType
RemittanceTask: EnumMsgType
WalletBalanceTask: EnumMsgType
WalletBalanceTaskResultNotice: EnumMsgType
AddFriendNotice: EnumMsgType
QueryHbDetailTask: EnumMsgType
QueryHbDetailTaskResultNotice: EnumMsgType
JoinGroupByQrTask: EnumMsgType
SendJielongTask: EnumMsgType
CDNDownloadFileTask: EnumMsgType
ContactSetLabelTask: EnumMsgType
CDNDownloadResultNotice: EnumMsgType
PullEmojiInfoTask: EnumMsgType
PullEmojiInfoTaskResultNotice: EnumMsgType
TriggerCircleMsgPushTask: EnumMsgType
CircleMsgReadTask: EnumMsgType
CircleMsgClearTask: EnumMsgType
GetContactInfoTask: EnumMsgType
ContactInfoNotice: EnumMsgType
GetFriendDetectResult: EnumMsgType
FriendDetectResultNotice: EnumMsgType
TriggerUnReadTask: EnumMsgType
ScreenShotTask: EnumMsgType
ScreenShotTaskResultNotice: EnumMsgType
GetA8KeyTask: EnumMsgType
TriggerQwUserPush: EnumMsgType
QwUserPUshNotice: EnumMsgType
QueryHbStatusTask: EnumMsgType
QueryHbStatusTaskResultNotice: EnumMsgType
SendSmsTask: EnumMsgType
CallLogPushNotice: EnumMsgType
SmsPushNotice: EnumMsgType
SmsReadNotice: EnumMsgType
SmsSentNotice: EnumMsgType
PullSmsTask: EnumMsgType
PullSmsTaskResultNotice: EnumMsgType
PullCallLogTask: EnumMsgType
PullCallLogTaskResultNotice: EnumMsgType
TriggerConfigPush: EnumMsgType
ConfigPushNotice: EnumMsgType
SetConfigTask: EnumMsgType
FriendPushNotice: EnumMsgType
PostDeviceInfoNotice: EnumMsgType
PostFriendDetectCountNotice: EnumMsgType
CirclePushNotice: EnumMsgType
OneKeyLikeTaskResultNotice: EnumMsgType
ChatroomPushNotice: EnumMsgType
ContactLabelInfoNotice: EnumMsgType
HistoryMsgPushNotice: EnumMsgType
ChatRoomMembersNotice: EnumMsgType
ConversationPushNotice: EnumMsgType
FriendAddReqListNotice: EnumMsgType
BizContactPushNotice: EnumMsgType
BizContactAddNotice: EnumMsgType
CircleMsgPushNotice: EnumMsgType
QwConversPushNotice: EnumMsgType
BizConversPushNotice: EnumMsgType
GetWeChatsReq: EnumMsgType
GetWeChatsRsp: EnumMsgType
RecentFriendChangeNotice: EnumMsgType
TodayFriendChangeNotice: EnumMsgType
AccountLogoutNotice: EnumMsgType
WeChatLoginNotice: EnumMsgType
SyncFriendListAsyncReq: EnumMsgType
SyncFriendListAsyncRsp: EnumMsgType
SyncRecentFriendListAsyncReq: EnumMsgType
SyncRecentFriendListAsyncRsp: EnumMsgType
SyncTodayFriendListAsyncReq: EnumMsgType
SyncTodayFriendListAsyncRsp: EnumMsgType
SyncFriendMessageAsyncReq: EnumMsgType
SyncFriendMessageAsyncRsp: EnumMsgType
TalkToFriendTaskReceived: EnumMsgType
ReadChatMessageNotice: EnumMsgType
SyncFriendAddReqeustAsyncReq: EnumMsgType
SyncFriendAddRequestAsyncRsp: EnumMsgType
WeChatForceOfflineNotice: EnumMsgType
SyncQuickReplyAsyncReq: EnumMsgType
SyncQuickReplyAsyncRsp: EnumMsgType
QuickReplyAddNotice: EnumMsgType
QuickReplyAddReceived: EnumMsgType
QuickReplyDelNotice: EnumMsgType
GetTagGroupReq: EnumMsgType
GetTagGroupRsp: EnumMsgType
GetTagFriendsReq: EnumMsgType
GetTagFriendsRsp: EnumMsgType
WeChatForceOnlineNotice: EnumMsgType
DeleteRecentFriendNotice: EnumMsgType
DeleteTodayFriendNotice: EnumMsgType
WeChatInfoChangeNotice: EnumMsgType
GetLastestVersionReq: EnumMsgType
GetLastestVersionRsp: EnumMsgType
CheckDeviceAppVersionReq: EnumMsgType
CheckDeviceAppVersionRsp: EnumMsgType
NewAppVersionPublishNotice: EnumMsgType
WeChatLoginNoticeResp: EnumMsgType
GroupMemberAddProgress: EnumMsgType
PostAppInfoReq: EnumMsgType
PostLogReq: EnumMsgType
Success: EnumErrorCode
NoRight: EnumErrorCode
InvalidParam: EnumErrorCode
InternalError: EnumErrorCode
TargetNotOnline: EnumErrorCode
UnknownGender: EnumGender
Male: EnumGender
Female: EnumGender
UnknownContent: EnumContentType
Text: EnumContentType
Picture: EnumContentType
Voice: EnumContentType
Video: EnumContentType
System: EnumContentType
Link: EnumContentType
LinkExt: EnumContentType
File: EnumContentType
NameCard: EnumContentType
Location: EnumContentType
LuckyMoney: EnumContentType
MoneyTrans: EnumContentType
WeApp: EnumContentType
Emoji: EnumContentType
RoomManage: EnumContentType
Sys_LuckyMoney: EnumContentType
RoomSystem: EnumContentType
BizLink: EnumContentType
AudioCall: EnumContentType
VideoCall: EnumContentType
NotifyMsg: EnumContentType
QuoteMsg: EnumContentType
JieLongMsg: EnumContentType
ShiPinHao: EnumContentType
RoomLiving: EnumContentType
PaiYiPai: EnumContentType
FinderLive: EnumContentType
KefuNameCard: EnumContentType
QiyeNameCard: EnumContentType
UnSupport: EnumContentType
UnknownState: EnumOnlineState
Online: EnumOnlineState
Offline: EnumOnlineState
UnknownTask: EnumTaskType
ReadTencentNews: EnumTaskType
ReadMPArticles: EnumTaskType
ReadKYKArticles: EnumTaskType
UnknownAccountType: EnumAccountType
Main: EnumAccountType
SubUser: EnumAccountType
NoAction: EnumSendStatus
Sending: EnumSendStatus
SendSuccess: EnumSendStatus
SendError: EnumSendStatus
NoReason: EnumForceOfflineReason
FuckedByOtherAuthorizer: EnumForceOfflineReason
ByReAlloc: EnumForceOfflineReason
ByDeviceOffline: EnumForceOfflineReason
ByWeChatOffline: EnumForceOfflineReason

class TransportMessage(_message.Message):
    __slots__ = ("Id", "AccessToken", "MsgType", "Content", "RefMessageId")
    ID_FIELD_NUMBER: _ClassVar[int]
    ACCESSTOKEN_FIELD_NUMBER: _ClassVar[int]
    MSGTYPE_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    REFMESSAGEID_FIELD_NUMBER: _ClassVar[int]
    Id: int
    AccessToken: str
    MsgType: EnumMsgType
    Content: _any_pb2.Any
    RefMessageId: int
    def __init__(self, Id: _Optional[int] = ..., AccessToken: _Optional[str] = ..., MsgType: _Optional[_Union[EnumMsgType, str]] = ..., Content: _Optional[_Union[_any_pb2.Any, _Mapping]] = ..., RefMessageId: _Optional[int] = ...) -> None: ...