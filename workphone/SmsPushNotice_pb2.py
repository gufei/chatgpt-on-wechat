# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: SmsPushNotice.proto
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
    'SmsPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13SmsPushNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x97\x01\n\nSmsMessage\x12\n\n\x02Id\x18\x01 \x01(\x05\x12\x0e\n\x06Number\x18\x02 \x01(\t\x12\x0c\n\x04Type\x18\x03 \x01(\x05\x12\x0c\n\x04\x44\x61te\x18\x04 \x01(\x03\x12\x0f\n\x07\x43ontent\x18\x05 \x01(\t\x12\x0c\n\x04Read\x18\x06 \x01(\x08\x12\x10\n\x08ThreadId\x18\x07 \x01(\x05\x12\r\n\x05SimId\x18\x08 \x01(\x05\x12\x11\n\tBlockType\x18\t \x01(\x05\"m\n\x14SmsPushNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x0c\n\x04IMEI\x18\x02 \x01(\t\x12\x35\n\x08Messages\x18\x03 \x01(\x0b\x32#.Jubo.JuLiao.IM.Wx.Proto.SmsMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'SmsPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_SMSMESSAGE']._serialized_start=49
  _globals['_SMSMESSAGE']._serialized_end=200
  _globals['_SMSPUSHNOTICEMESSAGE']._serialized_start=202
  _globals['_SMSPUSHNOTICEMESSAGE']._serialized_end=311
# @@protoc_insertion_point(module_scope)
