# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WDownloadFileResultNotice.proto
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
    'WDownloadFileResultNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WTransport_pb2 as WTransport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1fWDownloadFileResultNotice.proto\x12\x10Im.Scrm.Ww.Proto\x1a\x10WTransport.proto\"\x9e\x01\n\x1f\x44ownloadFileResultNoticeMessage\x12\x0c\n\x04WxId\x18\x01 \x01(\x03\x12\x0f\n\x07Success\x18\x02 \x01(\x08\x12\x0e\n\x06\x45rrMsg\x18\x03 \x01(\t\x12\x0e\n\x06OrgUrl\x18\x04 \x01(\t\x12\x0b\n\x03Url\x18\x05 \x01(\t\x12\x10\n\x08\x46ileType\x18\x06 \x01(\x05\x12\x0e\n\x06TaskId\x18\x07 \x01(\x03\x12\r\n\x05MsgId\x18\x08 \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WDownloadFileResultNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DOWNLOADFILERESULTNOTICEMESSAGE']._serialized_start=72
  _globals['_DOWNLOADFILERESULTNOTICEMESSAGE']._serialized_end=230
# @@protoc_insertion_point(module_scope)
