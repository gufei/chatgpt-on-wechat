# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PhoneActionTask.proto
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
    'PhoneActionTask.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x15PhoneActionTask.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\xa6\x01\n\x16PhoneActionTaskMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x0c\n\x04Imei\x18\x02 \x01(\t\x12\x38\n\x06\x41\x63tion\x18\x03 \x01(\x0e\x32(.Jubo.JuLiao.IM.Wx.Proto.EnumPhoneAction\x12\x10\n\x08StrParam\x18\x04 \x01(\t\x12\x10\n\x08IntParam\x18\x05 \x01(\x05\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03*\xa0\x01\n\x0f\x45numPhoneAction\x12\x08\n\x04None\x10\x00\x12\n\n\x06Reboot\x10\x01\x12\r\n\tUploadLog\x10\x02\x12\x0e\n\nUploadFile\x10\x03\x12\x11\n\rCleanAppCache\x10\x04\x12\x10\n\x0c\x43leanWxCache\x10\x05\x12\x15\n\x11\x43leanFileUrlCache\x10\x06\x12\r\n\tPhoneCall\x10\x07\x12\r\n\tRestartWx\x10\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PhoneActionTask_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ENUMPHONEACTION']._serialized_start=220
  _globals['_ENUMPHONEACTION']._serialized_end=380
  _globals['_PHONEACTIONTASKMESSAGE']._serialized_start=51
  _globals['_PHONEACTIONTASKMESSAGE']._serialized_end=217
# @@protoc_insertion_point(module_scope)