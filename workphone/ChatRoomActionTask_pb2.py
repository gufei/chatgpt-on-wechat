# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ChatRoomActionTask.proto
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
    'ChatRoomActionTask.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18\x43hatRoomActionTask.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\xb1\x01\n\x19\x43hatRoomActionTaskMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x12\n\nChatRoomId\x18\x02 \x01(\t\x12;\n\x06\x41\x63tion\x18\x03 \x01(\x0e\x32+.Jubo.JuLiao.IM.Wx.Proto.EnumChatRoomAction\x12\x0f\n\x07\x43ontent\x18\x04 \x01(\t\x12\x10\n\x08IntValue\x18\x05 \x01(\x05\x12\x0e\n\x06taskId\x18\x06 \x01(\x03*\x9b\x02\n\x12\x45numChatRoomAction\x12\x0c\n\x08RoomName\x10\x00\x12\x14\n\x10ModifyPublicNoti\x10\x01\x12\r\n\tAddMember\x10\x02\x12\x0e\n\nKickMember\x10\x03\x12\x10\n\x0cRoomShowName\x10\x04\x12\x12\n\x0e\x41\x64\x64ToPhonebook\x10\x05\x12\x0e\n\nNewMsgNoti\x10\x06\x12\x0c\n\x08\x45xitRoom\x10\x07\x12\x0e\n\nCreateRoom\x10\x08\x12\x11\n\rViewAllMember\x10\t\x12\x11\n\rTransferOwner\x10\n\x12\r\n\tSetVerify\x10\x0b\x12\x0e\n\nAddManager\x10\x0c\x12\x0e\n\nDelManager\x10\r\x12\r\n\tSetRemark\x10\x0e\x12\n\n\x06SetTop\x10\x10\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ChatRoomActionTask_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENUMCHATROOMACTION']._serialized_start=234
  _globals['_ENUMCHATROOMACTION']._serialized_end=517
  _globals['_CHATROOMACTIONTASKMESSAGE']._serialized_start=54
  _globals['_CHATROOMACTIONTASKMESSAGE']._serialized_end=231
# @@protoc_insertion_point(module_scope)