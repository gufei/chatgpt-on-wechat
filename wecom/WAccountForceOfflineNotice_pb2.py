# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WAccountForceOfflineNotice.proto
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
    'WAccountForceOfflineNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WTransport_pb2 as WTransport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n WAccountForceOfflineNotice.proto\x12\x10Im.Scrm.Ww.Proto\x1a\x10WTransport.proto\"{\n AccountForceOfflineNoticeMessage\x12\x38\n\x06Reason\x18\x01 \x01(\x0e\x32(.Im.Scrm.Ww.Proto.EnumForceOfflineReason\x12\x0f\n\x07Message\x18\x02 \x01(\t\x12\x0c\n\x04WxId\x18\x03 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WAccountForceOfflineNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ACCOUNTFORCEOFFLINENOTICEMESSAGE']._serialized_start=72
  _globals['_ACCOUNTFORCEOFFLINENOTICEMESSAGE']._serialized_end=195
# @@protoc_insertion_point(module_scope)
