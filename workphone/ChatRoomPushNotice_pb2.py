# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ChatRoomPushNotice.proto
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
    'ChatRoomPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x43hatRoomPushNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x91\x03\n\x0f\x43hatRoomMessage\x12\x10\n\x08UserName\x18\x01 \x01(\t\x12\x10\n\x08NickName\x18\x02 \x01(\t\x12\x12\n\nMemberList\x18\x03 \x03(\t\x12\r\n\x05Owner\x18\x04 \x01(\t\x12\x0e\n\x06Notice\x18\x05 \x01(\t\x12Q\n\x0cShowNameList\x18\x06 \x03(\x0b\x32;.Jubo.JuLiao.IM.Wx.Proto.ChatRoomMessage.DisplayNameMessage\x12\x17\n\x0fSelfDisplayName\x18\x07 \x01(\t\x12\x0e\n\x06\x41vatar\x18\x08 \x01(\t\x12\x0e\n\x06Verify\x18\t \x01(\x05\x12\x11\n\tMsgSilent\x18\n \x01(\x08\x12\x0e\n\x06Remark\x18\x0b \x01(\t\x12\x0c\n\x04Type\x18\x0c \x01(\x05\x12\x11\n\tIsUnusual\x18\x1e \x01(\x08\x1aW\n\x12\x44isplayNameMessage\x12\x10\n\x08UserName\x18\x01 \x01(\t\x12\x10\n\x08ShowName\x18\x02 \x01(\t\x12\x0f\n\x07Inviter\x18\x03 \x01(\t\x12\x0c\n\x04\x46lag\x18\x04 \x01(\x05\"\xa5\x01\n\x19\x43hatRoomPushNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12;\n\tChatRooms\x18\x02 \x03(\x0b\x32(.Jubo.JuLiao.IM.Wx.Proto.ChatRoomMessage\x12\x0c\n\x04Size\x18\x03 \x01(\x05\x12\r\n\x05\x43ount\x18\x04 \x01(\x05\x12\x0c\n\x04Page\x18\x05 \x01(\x05\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatRoomPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CHATROOMMESSAGE']._serialized_start=54
  _globals['_CHATROOMMESSAGE']._serialized_end=455
  _globals['_CHATROOMMESSAGE_DISPLAYNAMEMESSAGE']._serialized_start=368
  _globals['_CHATROOMMESSAGE_DISPLAYNAMEMESSAGE']._serialized_end=455
  _globals['_CHATROOMPUSHNOTICEMESSAGE']._serialized_start=458
  _globals['_CHATROOMPUSHNOTICEMESSAGE']._serialized_end=623
# @@protoc_insertion_point(module_scope)