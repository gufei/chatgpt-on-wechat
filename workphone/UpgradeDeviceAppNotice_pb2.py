# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: UpgradeDeviceAppNotice.proto
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
    'UpgradeDeviceAppNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cUpgradeDeviceAppNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"f\n\x17\x44\x65viceAppUpgradeMessage\x12\x11\n\tVerNumber\x18\x01 \x01(\x05\x12\x0f\n\x07Version\x18\x02 \x01(\t\x12\x13\n\x0bPackageName\x18\x03 \x01(\t\x12\x12\n\nPackageUrl\x18\x04 \x01(\t\"\x83\x01\n\x1dUpgradeDeviceAppNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x0c\n\x04IMEI\x18\x02 \x01(\t\x12\x42\n\x08\x41ppInfos\x18\x03 \x03(\x0b\x32\x30.Jubo.JuLiao.IM.Wx.Proto.DeviceAppUpgradeMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'UpgradeDeviceAppNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_DEVICEAPPUPGRADEMESSAGE']._serialized_start=57
  _globals['_DEVICEAPPUPGRADEMESSAGE']._serialized_end=159
  _globals['_UPGRADEDEVICEAPPNOTICEMESSAGE']._serialized_start=162
  _globals['_UPGRADEDEVICEAPPNOTICEMESSAGE']._serialized_end=293
# @@protoc_insertion_point(module_scope)