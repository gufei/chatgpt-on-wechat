# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: ErrorMessage.proto
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
    'ErrorMessage.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TransportMessage_pb2 as TransportMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x12\x45rrorMessage.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x16TransportMessage.proto\"[\n\x0c\x45rrorMessage\x12\x39\n\tErrorCode\x18\x01 \x01(\x0e\x32&.Jubo.JuLiao.IM.Wx.Proto.EnumErrorCode\x12\x10\n\x08\x45rrorMsg\x18\x02 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'ErrorMessage_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ERRORMESSAGE']._serialized_start=71
  _globals['_ERRORMESSAGE']._serialized_end=162
# @@protoc_insertion_point(module_scope)
