# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GroupMemberAddProgress.proto
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
    'GroupMemberAddProgress.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1cGroupMemberAddProgress.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\xc5\x01\n\x1fGroupMemberAddTaskDetailMessage\x12\x0c\n\x04wxId\x18\x01 \x01(\t\x12\r\n\x05\x61lias\x18\x02 \x01(\t\x12\x10\n\x08nickname\x18\x03 \x01(\t\x12\x0e\n\x06\x61vatar\x18\x04 \x01(\t\x12\x0e\n\x06gender\x18\x05 \x01(\x05\x12\x0f\n\x07\x63ountry\x18\x06 \x01(\t\x12\x10\n\x08province\x18\x07 \x01(\t\x12\x0c\n\x04\x63ity\x18\x08 \x01(\t\x12\x12\n\nupdateTime\x18\t \x01(\x05\x12\x0e\n\x06status\x18\n \x01(\x05\"\xb7\x02\n\x1dGroupMemberAddProgressMessage\x12\x0e\n\x06status\x18\x01 \x01(\x05\x12\x13\n\x0bsuspendType\x18\x02 \x01(\x05\x12\x10\n\x08progress\x18\x03 \x01(\x01\x12\x15\n\rtotalQuantity\x18\x04 \x01(\x05\x12\x18\n\x10waitSendQuantity\x18\x05 \x01(\x05\x12\x17\n\x0fsendingQuantity\x18\x06 \x01(\x05\x12\x16\n\x0esendedQuantity\x18\x07 \x01(\x05\x12\x16\n\x0epassedQuantity\x18\x08 \x01(\x05\x12\x17\n\x0fignoredQuantity\x18\t \x01(\x05\x12L\n\ndetailList\x18\n \x03(\x0b\x32\x38.Jubo.JuLiao.IM.Wx.Proto.GroupMemberAddTaskDetailMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GroupMemberAddProgress_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_GROUPMEMBERADDTASKDETAILMESSAGE']._serialized_start=58
  _globals['_GROUPMEMBERADDTASKDETAILMESSAGE']._serialized_end=255
  _globals['_GROUPMEMBERADDPROGRESSMESSAGE']._serialized_start=258
  _globals['_GROUPMEMBERADDPROGRESSMESSAGE']._serialized_end=569
# @@protoc_insertion_point(module_scope)
