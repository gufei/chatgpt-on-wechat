# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: CircleMsgPushNotice.proto
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
    'CircleMsgPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import CircleNewPublishNotice_pb2 as CircleNewPublishNotice__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19\x43ircleMsgPushNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x1c\x43ircleNewPublishNotice.proto\"\xba\x01\n\x1a\x43ircleMsgPushNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12?\n\x08\x43omments\x18\x02 \x03(\x0b\x32-.Jubo.JuLiao.IM.Wx.Proto.CircleCommentMessage\x12\x39\n\x05Likes\x18\x03 \x03(\x0b\x32*.Jubo.JuLiao.IM.Wx.Proto.CircleLikeMessage\x12\x0e\n\x06TaskId\x18\x04 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CircleMsgPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CIRCLEMSGPUSHNOTICEMESSAGE']._serialized_start=85
  _globals['_CIRCLEMSGPUSHNOTICEMESSAGE']._serialized_end=271
# @@protoc_insertion_point(module_scope)