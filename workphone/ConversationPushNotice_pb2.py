# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ConversationPushNotice.proto
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
    'ConversationPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1c\x43onversationPushNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x84\x02\n\x0e\x43onversMessage\x12\x10\n\x08UserName\x18\x01 \x01(\t\x12\x0e\n\x06\x44igest\x18\x02 \x01(\t\x12\x12\n\nDigestUser\x18\x03 \x01(\t\x12\x0e\n\x06IsSend\x18\x04 \x01(\x08\x12\x0e\n\x06MsgCnt\x18\x05 \x01(\x05\x12\x11\n\tUnreadCnt\x18\x06 \x01(\x05\x12\x12\n\nUpdateTime\x18\x07 \x01(\x03\x12\r\n\x05IsTop\x18\x08 \x01(\x08\x12\x10\n\x08IsSilent\x18\t \x01(\x08\x12\x10\n\x08ShowName\x18\x0b \x01(\t\x12\x0e\n\x06\x41vatar\x18\x0c \x01(\t\x12\x0f\n\x07\x41tCount\x18\r \x01(\x05\x12\x0e\n\x06Remark\x18\x0f \x01(\t\x12\x11\n\tIsUnusual\x18\x1e \x01(\x08\"\xca\x01\n\x1d\x43onversationPushNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x38\n\x07\x43onvers\x18\x02 \x03(\x0b\x32\'.Jubo.JuLiao.IM.Wx.Proto.ConversMessage\x12\x0c\n\x04Size\x18\x03 \x01(\x05\x12\r\n\x05\x43ount\x18\x04 \x01(\x05\x12\x0c\n\x04Page\x18\x05 \x01(\x05\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\x12\x0e\n\x06Offset\x18\x07 \x01(\x05\x12\x12\n\nNextOffset\x18\x08 \x01(\x05\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ConversationPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONVERSMESSAGE']._serialized_start=58
  _globals['_CONVERSMESSAGE']._serialized_end=318
  _globals['_CONVERSATIONPUSHNOTICEMESSAGE']._serialized_start=321
  _globals['_CONVERSATIONPUSHNOTICEMESSAGE']._serialized_end=523
# @@protoc_insertion_point(module_scope)
