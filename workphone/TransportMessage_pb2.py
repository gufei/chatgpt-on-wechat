# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: TransportMessage.proto
# Protobuf Python Version: 5.28.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    28,
    3,
    '',
    'TransportMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16TransportMessage.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x19google/protobuf/any.proto\"\xa7\x01\n\x10TransportMessage\x12\n\n\x02Id\x18\x01 \x01(\x03\x12\x13\n\x0b\x41\x63\x63\x65ssToken\x18\x02 \x01(\t\x12\x35\n\x07MsgType\x18\x03 \x01(\x0e\x32$.Jubo.JuLiao.IM.Wx.Proto.EnumMsgType\x12%\n\x07\x43ontent\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\x12\x14\n\x0cRefMessageId\x18\x05 \x01(\x03*\xab,\n\x0b\x45numMsgType\x12\x0e\n\nUnknownMsg\x10\x00\x12\x11\n\x0cHeartBeatReq\x10\xe9\x07\x12\x13\n\x0eMsgReceivedAck\x10\xea\x07\x12\n\n\x05\x45rror\x10\xeb\x07\x12\x12\n\rDeviceAuthReq\x10\xf2\x07\x12\x12\n\rDeviceAuthRsp\x10\xf3\x07\x12\x15\n\x10\x44\x65viceExitNotice\x10\xf4\x07\x12\x1e\n\x19\x41\x63\x63ountForceOfflineNotice\x10\xf5\x07\x12\x13\n\x0eRedirectNotice\x10\xf7\x07\x12\x16\n\x11TriggerDeviceInfo\x10\xf8\x07\x12\x1a\n\x15TriggerWechatPushTask\x10\xfb\x07\x12\x17\n\x12WeChatOnlineNotice\x10\xfc\x07\x12\x18\n\x13WeChatOfflineNotice\x10\xfd\x07\x12\x14\n\x0f\x46riendAddNotice\x10\xfe\x07\x12\x14\n\x0f\x46riendDelNotice\x10\xff\x07\x12\x15\n\x10\x46riendTalkNotice\x10\x80\x08\x12\x15\n\x10TaskResultNotice\x10\x81\x08\x12\x1d\n\x18WeChatTalkToFriendNotice\x10\x82\x08\x12\x1b\n\x16\x46riendAddReqeustNotice\x10\x83\x08\x12!\n\x1cTalkToFriendTaskResultNotice\x10\x84\x08\x12&\n!RequestTalkDetailTaskResultNotice\x10\x85\x08\x12%\n PullWeChatQrCodeTaskResultNotice\x10\x86\x08\x12\x1b\n\x16\x43ircleNewPublishNotice\x10\x87\x08\x12\x14\n\x0f\x43ircleDelNotice\x10\x88\x08\x12\x15\n\x10\x43ircleLikeNotice\x10\x89\x08\x12\x18\n\x13\x43ircleCommentNotice\x10\x8a\x08\x12\x1a\n\x15PostMessageReadNotice\x10\x8b\x08\x12\x16\n\x11\x43hatRoomAddNotice\x10\x8d\x08\x12\x1a\n\x15\x43ontactLabelAddNotice\x10\x8e\x08\x12\x1e\n\x19TakeMoneyTaskResultNotice\x10\x8f\x08\x12\x17\n\x12\x43ircleDetailNotice\x10\x90\x08\x12\x16\n\x11\x43hatRoomDelNotice\x10\x91\x08\x12\x1a\n\x15\x43hatRoomChangedNotice\x10\x92\x08\x12\'\n\"PullChatRoomQrCodeTaskResultNotice\x10\x93\x08\x12\x1a\n\x15\x43ontactLabelDelNotice\x10\x94\x08\x12\x19\n\x14\x43hatMsgIdsPushNotice\x10\x9a\x08\x12\x1a\n\x15\x43hatMsgFilePushNotice\x10\x9b\x08\x12\x17\n\x12\x46riendChangeNotice\x10\x9c\x08\x12\x1c\n\x17PhoneStateWarningNotice\x10\x9d\x08\x12\x11\n\x0cMsgDelNotice\x10\x9e\x08\x12\x12\n\rConvDelNotice\x10\x9f\x08\x12\x15\n\x10TalkToFriendTask\x10\xae\x08\x12\x14\n\x0fPostSNSNewsTask\x10\xaf\x08\x12\x13\n\x0e\x41\x64\x64\x46riendsTask\x10\xb0\x08\x12 \n\x1bPostSNSNewsTaskResultNotice\x10\xb1\x08\x12\x16\n\x11\x44\x65leteSNSNewsTask\x10\xb2\x08\x12\x1f\n\x1a\x41\x63\x63\x65ptFriendAddRequestTask\x10\xb3\x08\x12\x18\n\x13WeChatGroupSendTask\x10\xb4\x08\x12\x1a\n\x15RequestTalkDetailTask\x10\xb6\x08\x12\x19\n\x14PullWeChatQrCodeTask\x10\xb7\x08\x12\x1a\n\x15TriggerFriendPushTask\x10\xb8\x08\x12\x1a\n\x15TriggerCirclePushTask\x10\xb9\x08\x12\x1c\n\x17\x43ircleCommentDeleteTask\x10\xba\x08\x12(\n#CircleCommentDeleteTaskResultNotice\x10\xbb\x08\x12\x1b\n\x16\x43ircleCommentReplyTask\x10\xbc\x08\x12\'\n\"CircleCommentReplyTaskResultNotice\x10\xbd\x08\x12\x1b\n\x16TriggerMessageReadTask\x10\xbe\x08\x12\x16\n\x11RevokeMessageTask\x10\xbf\x08\x12\x17\n\x12\x46orwardMessageTask\x10\xc0\x08\x12\x1e\n\x19TriggerHistoryMsgPushTask\x10\xc1\x08\x12\x1b\n\x16PullChatRoomQrCodeTask\x10\xc2\x08\x12\x19\n\x14SendMultiPictureTask\x10\xc3\x08\x12\x1c\n\x17\x46orwardMultiMessageTask\x10\xc4\x08\x12\x15\n\x10UpgradeAppNotice\x10\xc5\x08\x12\x1b\n\x16UpgradeDeviceAppNotice\x10\xc6\x08\x12\x19\n\x14PostFriendDetectTask\x10\xc7\x08\x12\x1d\n\x18PostStopFriendDetectTask\x10\xc8\x08\x12\x1b\n\x16PostDeleteDeviceNotice\x10\xc9\x08\x12\x13\n\x0eOneKeyLikeTask\x10\xca\x08\x12\x19\n\x14ModifyFriendMemoTask\x10\xcd\x08\x12\x1b\n\x16\x41\x64\x64\x46riendWithSceneTask\x10\xce\x08\x12\x17\n\x12TakeLuckyMoneyTask\x10\xb0\t\x12\x19\n\x14PullFriendCircleTask\x10\xb1\t\x12\x19\n\x14PullCircleDetailTask\x10\xb2\t\x12\x13\n\x0e\x43ircleLikeTask\x10\xb3\t\x12\x1c\n\x17TriggerChatroomPushTask\x10\xba\t\x12\x1c\n\x17RequestChatRoomInfoTask\x10\xbb\t\x12\x1c\n\x17RequestContactsInfoTask\x10\xbc\t\x12\x17\n\x12\x43hatRoomActionTask\x10\xbd\t\x12\x1c\n\x17\x41\x64\x64\x46riendInChatRoomTask\x10\xbe\t\x12\x1f\n\x1a\x41\x64\x64\x46riendFromPhonebookTask\x10\xbf\t\x12\x15\n\x10\x44\x65leteFriendTask\x10\xc0\t\x12\x17\n\x12SendLuckyMoneyTask\x10\xc1\t\x12\x1b\n\x16RequestTalkContentTask\x10\xc2\t\x12\'\n\"RequestTalkContentTaskResultNotice\x10\xc3\t\x12 \n\x1b\x46orwardMessageByContentTask\x10\xc4\t\x12\x1e\n\x19\x43hatRoomInviteApproveTask\x10\xc5\t\x12\x15\n\x10WechatLogoutTask\x10\xc6\t\x12\x14\n\x0fPhoneActionTask\x10\xc7\t\x12\x15\n\x10\x43ontactLabelTask\x10\xc8\t\x12\x1b\n\x16\x43ontactLabelDeleteTask\x10\xc9\t\x12\x17\n\x12VoiceTransTextTask\x10\xca\t\x12\x14\n\x0f\x46indContactTask\x10\xcb\t\x12\x1a\n\x15\x46indContactTaskResult\x10\xcc\t\x12\x1a\n\x15\x41greeJoinChatRoomTask\x10\xcd\t\x12\x18\n\x13\x43learAllChatMsgTask\x10\xce\t\x12\x19\n\x14SendFriendVerifyTask\x10\xcf\t\x12 \n\x1bTriggerConversationPushTask\x10\xd0\t\x12\x16\n\x11WechatSettingTask\x10\xd1\t\x12\x1d\n\x18PullFriendAddReqListTask\x10\xd2\t\x12\x1e\n\x19TriggerBizContactPushTask\x10\xd3\t\x12\x1a\n\x15\x41\x64\x64\x46riendNameCardTask\x10\xd4\t\x12\x1e\n\x19TriggerChatMsgIdsPushTask\x10\xe3\t\x12\x17\n\x12RequestTalkMsgTask\x10\xe4\t\x12#\n\x1eRequestTalkMsgTaskResultNotice\x10\xe5\t\x12\x19\n\x14SearchBizContactTask\x10\xe6\t\x12%\n SearchBizContactTaskResultNotice\x10\xe7\t\x12\x13\n\x0ePhoneStateTask\x10\xe8\t\x12\x1f\n\x1aPhoneStateTaskResultNotice\x10\xe9\t\x12\x17\n\x12WeChatLocationTask\x10\xea\t\x12#\n\x1eWeChatLocationTaskResultNotice\x10\xeb\t\x12\x13\n\x0eRemittanceTask\x10\xec\t\x12\x16\n\x11WalletBalanceTask\x10\xee\t\x12\"\n\x1dWalletBalanceTaskResultNotice\x10\xef\t\x12\x14\n\x0f\x41\x64\x64\x46riendNotice\x10\xf0\t\x12\x16\n\x11QueryHbDetailTask\x10\xf1\t\x12\"\n\x1dQueryHbDetailTaskResultNotice\x10\xf2\t\x12\x16\n\x11JoinGroupByQrTask\x10\xf3\t\x12\x14\n\x0fSendJielongTask\x10\xf4\t\x12\x18\n\x13\x43\x44NDownloadFileTask\x10\xf5\t\x12\x18\n\x13\x43ontactSetLabelTask\x10\xf6\t\x12\x1c\n\x17\x43\x44NDownloadResultNotice\x10\xf7\t\x12\x16\n\x11PullEmojiInfoTask\x10\xf8\t\x12\"\n\x1dPullEmojiInfoTaskResultNotice\x10\xf9\t\x12\x1d\n\x18TriggerCircleMsgPushTask\x10\xfa\t\x12\x16\n\x11\x43ircleMsgReadTask\x10\xfb\t\x12\x17\n\x12\x43ircleMsgClearTask\x10\xfc\t\x12\x17\n\x12GetContactInfoTask\x10\xfd\t\x12\x16\n\x11\x43ontactInfoNotice\x10\xfe\t\x12\x1a\n\x15GetFriendDetectResult\x10\xff\t\x12\x1d\n\x18\x46riendDetectResultNotice\x10\x80\n\x12\x16\n\x11TriggerUnReadTask\x10\x81\n\x12\x13\n\x0eScreenShotTask\x10\x82\n\x12\x1f\n\x1aScreenShotTaskResultNotice\x10\x83\n\x12\x11\n\x0cGetA8KeyTask\x10\x84\n\x12\x16\n\x11TriggerQwUserPush\x10\x85\n\x12\x15\n\x10QwUserPUshNotice\x10\x86\n\x12\x16\n\x11QueryHbStatusTask\x10\x87\n\x12\"\n\x1dQueryHbStatusTaskResultNotice\x10\x88\n\x12\x10\n\x0bSendSmsTask\x10\x89\n\x12\x16\n\x11\x43\x61llLogPushNotice\x10\x94\n\x12\x12\n\rSmsPushNotice\x10\x95\n\x12\x12\n\rSmsReadNotice\x10\x96\n\x12\x12\n\rSmsSentNotice\x10\x97\n\x12\x10\n\x0bPullSmsTask\x10\x98\n\x12\x1c\n\x17PullSmsTaskResultNotice\x10\x99\n\x12\x14\n\x0fPullCallLogTask\x10\x9a\n\x12 \n\x1bPullCallLogTaskResultNotice\x10\x9b\n\x12\x16\n\x11TriggerConfigPush\x10\xe4\n\x12\x15\n\x10\x43onfigPushNotice\x10\xe5\n\x12\x12\n\rSetConfigTask\x10\xe6\n\x12\x15\n\x10\x46riendPushNotice\x10\xea\x0f\x12\x19\n\x14PostDeviceInfoNotice\x10\xeb\x0f\x12 \n\x1bPostFriendDetectCountNotice\x10\xec\x0f\x12\x15\n\x10\x43irclePushNotice\x10\xed\x0f\x12\x1f\n\x1aOneKeyLikeTaskResultNotice\x10\xee\x0f\x12\x17\n\x12\x43hatroomPushNotice\x10\xef\x0f\x12\x1b\n\x16\x43ontactLabelInfoNotice\x10\xf0\x0f\x12\x19\n\x14HistoryMsgPushNotice\x10\xf1\x0f\x12\x1a\n\x15\x43hatRoomMembersNotice\x10\xf2\x0f\x12\x1b\n\x16\x43onversationPushNotice\x10\xf3\x0f\x12\x1b\n\x16\x46riendAddReqListNotice\x10\xf4\x0f\x12\x19\n\x14\x42izContactPushNotice\x10\xf5\x0f\x12\x18\n\x13\x42izContactAddNotice\x10\xf6\x0f\x12\x18\n\x13\x43ircleMsgPushNotice\x10\xf7\x0f\x12\x18\n\x13QwConversPushNotice\x10\xf8\x0f\x12\x19\n\x14\x42izConversPushNotice\x10\xf9\x0f\x12\x12\n\rGetWeChatsReq\x10\xea\x17\x12\x12\n\rGetWeChatsRsp\x10\xeb\x17\x12\x1d\n\x18RecentFriendChangeNotice\x10\xec\x17\x12\x1c\n\x17TodayFriendChangeNotice\x10\xed\x17\x12\x18\n\x13\x41\x63\x63ountLogoutNotice\x10\xee\x17\x12\x16\n\x11WeChatLoginNotice\x10\xef\x17\x12\x1b\n\x16SyncFriendListAsyncReq\x10\xf0\x17\x12\x1b\n\x16SyncFriendListAsyncRsp\x10\xf1\x17\x12!\n\x1cSyncRecentFriendListAsyncReq\x10\xf2\x17\x12!\n\x1cSyncRecentFriendListAsyncRsp\x10\xf3\x17\x12 \n\x1bSyncTodayFriendListAsyncReq\x10\xf4\x17\x12 \n\x1bSyncTodayFriendListAsyncRsp\x10\xf5\x17\x12\x1e\n\x19SyncFriendMessageAsyncReq\x10\xf6\x17\x12\x1e\n\x19SyncFriendMessageAsyncRsp\x10\xf7\x17\x12\x1d\n\x18TalkToFriendTaskReceived\x10\xf8\x17\x12\x1a\n\x15ReadChatMessageNotice\x10\xf9\x17\x12!\n\x1cSyncFriendAddReqeustAsyncReq\x10\xfa\x17\x12!\n\x1cSyncFriendAddRequestAsyncRsp\x10\xfb\x17\x12\x1d\n\x18WeChatForceOfflineNotice\x10\xfc\x17\x12\x1b\n\x16SyncQuickReplyAsyncReq\x10\xfd\x17\x12\x1b\n\x16SyncQuickReplyAsyncRsp\x10\xfe\x17\x12\x18\n\x13QuickReplyAddNotice\x10\xff\x17\x12\x1a\n\x15QuickReplyAddReceived\x10\x80\x18\x12\x18\n\x13QuickReplyDelNotice\x10\x81\x18\x12\x13\n\x0eGetTagGroupReq\x10\x82\x18\x12\x13\n\x0eGetTagGroupRsp\x10\x83\x18\x12\x15\n\x10GetTagFriendsReq\x10\x84\x18\x12\x15\n\x10GetTagFriendsRsp\x10\x85\x18\x12\x1c\n\x17WeChatForceOnlineNotice\x10\x86\x18\x12\x1d\n\x18\x44\x65leteRecentFriendNotice\x10\x87\x18\x12\x1c\n\x17\x44\x65leteTodayFriendNotice\x10\x88\x18\x12\x1b\n\x16WeChatInfoChangeNotice\x10\x89\x18\x12\x19\n\x14GetLastestVersionReq\x10\x8a\x18\x12\x19\n\x14GetLastestVersionRsp\x10\x8b\x18\x12\x1d\n\x18\x43heckDeviceAppVersionReq\x10\x8c\x18\x12\x1d\n\x18\x43heckDeviceAppVersionRsp\x10\x8d\x18\x12\x1f\n\x1aNewAppVersionPublishNotice\x10\x8e\x18\x12\x1a\n\x15WeChatLoginNoticeResp\x10\x8f\x18\x12\x1b\n\x16GroupMemberAddProgress\x10\x91\x18\x12\x13\n\x0ePostAppInfoReq\x10\x81\x19\x12\x0f\n\nPostLogReq\x10\x82\x19*g\n\rEnumErrorCode\x12\x0b\n\x07Success\x10\x00\x12\x0c\n\x07NoRight\x10\xe9\x07\x12\x11\n\x0cInvalidParam\x10\xea\x07\x12\x12\n\rInternalError\x10\xeb\x07\x12\x14\n\x0fTargetNotOnline\x10\xec\x07*5\n\nEnumGender\x12\x11\n\rUnknownGender\x10\x00\x12\x08\n\x04Male\x10\x01\x12\n\n\x06\x46\x65male\x10\x02*\xcd\x03\n\x0f\x45numContentType\x12\x12\n\x0eUnknownContent\x10\x00\x12\x08\n\x04Text\x10\x01\x12\x0b\n\x07Picture\x10\x02\x12\t\n\x05Voice\x10\x03\x12\t\n\x05Video\x10\x04\x12\n\n\x06System\x10\x05\x12\x08\n\x04Link\x10\x06\x12\x0b\n\x07LinkExt\x10\x07\x12\x08\n\x04\x46ile\x10\x08\x12\x0c\n\x08NameCard\x10\t\x12\x0c\n\x08Location\x10\n\x12\x0e\n\nLuckyMoney\x10\x0b\x12\x0e\n\nMoneyTrans\x10\x0c\x12\t\n\x05WeApp\x10\r\x12\t\n\x05\x45moji\x10\x0e\x12\x0e\n\nRoomManage\x10\x0f\x12\x12\n\x0eSys_LuckyMoney\x10\x10\x12\x0e\n\nRoomSystem\x10\x11\x12\x0b\n\x07\x42izLink\x10\x12\x12\r\n\tAudioCall\x10\x13\x12\r\n\tVideoCall\x10\x14\x12\r\n\tNotifyMsg\x10\x15\x12\x0c\n\x08QuoteMsg\x10\x16\x12\x0e\n\nJieLongMsg\x10\x17\x12\r\n\tShiPinHao\x10\x18\x12\x0e\n\nRoomLiving\x10\x19\x12\x0c\n\x08PaiYiPai\x10\x1a\x12\x0e\n\nFinderLive\x10\x1c\x12\x10\n\x0cKefuNameCard\x10\x1d\x12\x10\n\x0cQiyeNameCard\x10\x1e\x12\r\n\tUnSupport\x10\x63*<\n\x0f\x45numOnlineState\x12\x10\n\x0cUnknownState\x10\x00\x12\n\n\x06Online\x10\x01\x12\x0b\n\x07Offline\x10\x02*]\n\x0c\x45numTaskType\x12\x0f\n\x0bUnknownTask\x10\x00\x12\x13\n\x0fReadTencentNews\x10\x01\x12\x12\n\x0eReadMPArticles\x10\x02\x12\x13\n\x0fReadKYKArticles\x10\x03*@\n\x0f\x45numAccountType\x12\x16\n\x12UnknownAccountType\x10\x00\x12\x08\n\x04Main\x10\x01\x12\x0b\n\x07SubUser\x10\x02*K\n\x0e\x45numSendStatus\x12\x0c\n\x08NoAction\x10\x00\x12\x0b\n\x07Sending\x10\x01\x12\x0f\n\x0bSendSuccess\x10\x11\x12\r\n\tSendError\x10\x10*|\n\x16\x45numForceOfflineReason\x12\x0c\n\x08NoReason\x10\x00\x12\x1b\n\x17\x46uckedByOtherAuthorizer\x10\x01\x12\r\n\tByReAlloc\x10\x02\x12\x13\n\x0f\x42yDeviceOffline\x10\x03\x12\x13\n\x0f\x42yWeChatOffline\x10\x04\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'TransportMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENUMMSGTYPE']._serialized_start=249
  _globals['_ENUMMSGTYPE']._serialized_end=5924
  _globals['_ENUMERRORCODE']._serialized_start=5926
  _globals['_ENUMERRORCODE']._serialized_end=6029
  _globals['_ENUMGENDER']._serialized_start=6031
  _globals['_ENUMGENDER']._serialized_end=6084
  _globals['_ENUMCONTENTTYPE']._serialized_start=6087
  _globals['_ENUMCONTENTTYPE']._serialized_end=6548
  _globals['_ENUMONLINESTATE']._serialized_start=6550
  _globals['_ENUMONLINESTATE']._serialized_end=6610
  _globals['_ENUMTASKTYPE']._serialized_start=6612
  _globals['_ENUMTASKTYPE']._serialized_end=6705
  _globals['_ENUMACCOUNTTYPE']._serialized_start=6707
  _globals['_ENUMACCOUNTTYPE']._serialized_end=6771
  _globals['_ENUMSENDSTATUS']._serialized_start=6773
  _globals['_ENUMSENDSTATUS']._serialized_end=6848
  _globals['_ENUMFORCEOFFLINEREASON']._serialized_start=6850
  _globals['_ENUMFORCEOFFLINEREASON']._serialized_end=6974
  _globals['_TRANSPORTMESSAGE']._serialized_start=79
  _globals['_TRANSPORTMESSAGE']._serialized_end=246
# @@protoc_insertion_point(module_scope)
