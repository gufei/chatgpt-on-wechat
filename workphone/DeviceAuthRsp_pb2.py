# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: DeviceAuthRsp.proto
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
    'DeviceAuthRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TransportMessage_pb2 as TransportMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x44\x65viceAuthRsp.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x16TransportMessage.proto\"\xa2\x02\n\x14\x44\x65viceAuthRspMessage\x12\x13\n\x0b\x41\x63\x63\x65ssToken\x18\x01 \x01(\t\x12I\n\x05\x45xtra\x18\x02 \x01(\x0b\x32:.Jubo.JuLiao.IM.Wx.Proto.DeviceAuthRspMessage.ExtraMessage\x1a\xa9\x01\n\x0c\x45xtraMessage\x12\x12\n\nSupplierId\x18\x01 \x01(\x03\x12\x0f\n\x07UnionId\x18\x02 \x01(\x03\x12=\n\x0b\x41\x63\x63ountType\x18\x03 \x01(\x0e\x32(.Jubo.JuLiao.IM.Wx.Proto.EnumAccountType\x12\x14\n\x0cSupplierName\x18\x04 \x01(\t\x12\x10\n\x08NickName\x18\x05 \x01(\t\x12\r\n\x05Token\x18\x06 \x01(\tb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'DeviceAuthRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEVICEAUTHRSPMESSAGE']._serialized_start=73
  _globals['_DEVICEAUTHRSPMESSAGE']._serialized_end=363
  _globals['_DEVICEAUTHRSPMESSAGE_EXTRAMESSAGE']._serialized_start=194
  _globals['_DEVICEAUTHRSPMESSAGE_EXTRAMESSAGE']._serialized_end=363
# @@protoc_insertion_point(module_scope)
