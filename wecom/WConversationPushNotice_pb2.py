# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WConversationPushNotice.proto
# Protobuf Python Version: 5.29.3
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    3,
    '',
    'WConversationPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WTransport_pb2 as WTransport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1dWConversationPushNotice.proto\x12\x10Im.Scrm.Ww.Proto\x1a\x10WTransport.proto\"\xd2\x01\n\x1d\x43onversationPushNoticeMessage\x12\x0c\n\x04WxId\x18\x01 \x01(\x03\x12\x36\n\x07\x43onvers\x18\x02 \x03(\x0b\x32%.Im.Scrm.Ww.Proto.ConversationMessage\x12\x0c\n\x04Size\x18\x03 \x01(\x05\x12\r\n\x05\x43ount\x18\x04 \x01(\x05\x12\x0c\n\x04Page\x18\x05 \x01(\x05\x12\r\n\x05IsEnd\x18\x06 \x01(\x08\x12\x12\n\nNextOffset\x18\x07 \x01(\x05\x12\r\n\x05Total\x18\x08 \x01(\x05\x12\x0e\n\x06TaskId\x18\t \x01(\x03\"\x9e\x03\n\x13\x43onversationMessage\x12\n\n\x02Id\x18\x01 \x01(\x03\x12\x10\n\x08RemoteId\x18\x02 \x01(\x03\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\x0e\n\x06\x41vatar\x18\x04 \x01(\t\x12\x0c\n\x04Type\x18\x05 \x01(\x05\x12\x0f\n\x07\x43reator\x18\x06 \x01(\x03\x12\x12\n\nCreateTime\x18\x07 \x01(\x03\x12\x12\n\nUpdateTime\x18\x08 \x01(\x03\x12\x10\n\x08Notified\x18\t \x01(\x08\x12\x0c\n\x04\x46lag\x18\n \x01(\x05\x12\x11\n\tUnreadCnt\x18\x0b \x01(\x05\x12\x0e\n\x06Notice\x18\x0c \x01(\t\x12\x0e\n\x06\x44igest\x18\r \x01(\t\x12\x34\n\x07Members\x18\x0e \x03(\x0b\x32#.Im.Scrm.Ww.Proto.ConvMemberMessage\x12\x0e\n\x06\x41\x64mins\x18\x0f \x03(\x03\x12\x17\n\x0fHasExternMember\x18\x10 \x01(\x08\x12\x12\n\nAvatarList\x18\x11 \x03(\t\x12\x0f\n\x07isSaved\x18\x12 \x01(\x08\x12\x10\n\x08isMarked\x18\x13 \x01(\x08\x12\r\n\x05isTop\x18\x14 \x01(\x08\x12\x0c\n\x04\x46wId\x18\x15 \x01(\x03\"\x8c\x01\n\x11\x43onvMemberMessage\x12\x10\n\x08RemoteId\x18\x01 \x01(\x03\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x10\n\x08JoinTime\x18\x03 \x01(\x03\x12\x11\n\tJoinScene\x18\x04 \x01(\x05\x12\x0e\n\x06\x41vatar\x18\x05 \x01(\t\x12\x0e\n\x06\x43orpId\x18\x06 \x01(\x03\x12\x12\n\nOpRemoteId\x18\x07 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WConversationPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONVERSATIONPUSHNOTICEMESSAGE']._serialized_start=70
  _globals['_CONVERSATIONPUSHNOTICEMESSAGE']._serialized_end=280
  _globals['_CONVERSATIONMESSAGE']._serialized_start=283
  _globals['_CONVERSATIONMESSAGE']._serialized_end=697
  _globals['_CONVMEMBERMESSAGE']._serialized_start=700
  _globals['_CONVMEMBERMESSAGE']._serialized_end=840
# @@protoc_insertion_point(module_scope)
