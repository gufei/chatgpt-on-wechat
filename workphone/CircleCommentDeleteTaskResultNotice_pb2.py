# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: CircleCommentDeleteTaskResultNotice.proto
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
    'CircleCommentDeleteTaskResultNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TransportMessage_pb2 as TransportMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)CircleCommentDeleteTaskResultNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x16TransportMessage.proto\"\xca\x01\n*CircleCommentDeleteTaskResultNoticeMessage\x12\x0f\n\x07Success\x18\x01 \x01(\x08\x12\x34\n\x04\x43ode\x18\x02 \x01(\x0e\x32&.Jubo.JuLiao.IM.Wx.Proto.EnumErrorCode\x12\x0e\n\x06\x45rrMsg\x18\x03 \x01(\t\x12\x10\n\x08\x43ircleId\x18\x04 \x01(\x03\x12\x11\n\tCommentId\x18\x05 \x01(\x03\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\x12\x10\n\x08WeChatId\x18\x07 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CircleCommentDeleteTaskResultNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CIRCLECOMMENTDELETETASKRESULTNOTICEMESSAGE']._serialized_start=95
  _globals['_CIRCLECOMMENTDELETETASKRESULTNOTICEMESSAGE']._serialized_end=297
# @@protoc_insertion_point(module_scope)