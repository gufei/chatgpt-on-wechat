# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: RemittanceTask.proto
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
    'RemittanceTask.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14RemittanceTask.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x88\x01\n\x15RemittanceTaskMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x10\n\x08\x46riendId\x18\x02 \x01(\t\x12\r\n\x05Money\x18\x03 \x01(\x05\x12\x0e\n\x06Passwd\x18\x04 \x01(\t\x12\x0c\n\x04Memo\x18\x05 \x01(\t\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\x12\x0e\n\x06RoomId\x18\x07 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'RemittanceTask_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_REMITTANCETASKMESSAGE']._serialized_start=50
  _globals['_REMITTANCETASKMESSAGE']._serialized_end=186
# @@protoc_insertion_point(module_scope)
