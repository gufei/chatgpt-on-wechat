# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: CallLogPushNotice.proto
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
    'CallLogPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x17\x43\x61llLogPushNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x8c\x01\n\x0e\x43\x61llLogMessage\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0e\n\x06Number\x18\x02 \x01(\t\x12\x0c\n\x04Type\x18\x03 \x01(\x05\x12\x0c\n\x04\x44\x61te\x18\x04 \x01(\x03\x12\x10\n\x08\x44uration\x18\x05 \x01(\x05\x12\x0e\n\x06Record\x18\x06 \x01(\t\x12\r\n\x05SimId\x18\x07 \x01(\x05\x12\x11\n\tBlockType\x18\x08 \x01(\x05\"u\n\x18\x43\x61llLogPushNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x0c\n\x04IMEI\x18\x02 \x01(\t\x12\x39\n\x08Messages\x18\x03 \x01(\x0b\x32\'.Jubo.JuLiao.IM.Wx.Proto.CallLogMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'CallLogPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CALLLOGMESSAGE']._serialized_start=53
  _globals['_CALLLOGMESSAGE']._serialized_end=193
  _globals['_CALLLOGPUSHNOTICEMESSAGE']._serialized_start=195
  _globals['_CALLLOGPUSHNOTICEMESSAGE']._serialized_end=312
# @@protoc_insertion_point(module_scope)