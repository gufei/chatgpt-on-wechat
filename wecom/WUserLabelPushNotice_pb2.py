# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WUserLabelPushNotice.proto
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
    'WUserLabelPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WTransport_pb2 as WTransport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1aWUserLabelPushNotice.proto\x12\x10Im.Scrm.Ww.Proto\x1a\x10WTransport.proto\"\x98\x01\n\x1aUserLabelPushNoticeMessage\x12\x0c\n\x04WxId\x18\x01 \x01(\x03\x12<\n\x0bLabelGroups\x18\x02 \x03(\x0b\x32\'.Im.Scrm.Ww.Proto.UserLabelGroupMessage\x12\x0c\n\x04Page\x18\x03 \x01(\x05\x12\x10\n\x08\x46inished\x18\x04 \x01(\x08\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\"Q\n\x10UserLabelMessage\x12\n\n\x02Id\x18\x01 \x01(\x03\x12\x0c\n\x04Name\x18\x02 \x01(\t\x12\x12\n\nCreateTime\x18\x03 \x01(\x05\x12\x0f\n\x07GroupId\x18\x04 \x01(\x03\"\x84\x01\n\x15UserLabelGroupMessage\x12\n\n\x02Id\x18\x01 \x01(\x03\x12\x0f\n\x07\x43reator\x18\x02 \x01(\x03\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\x0c\n\x04Type\x18\x04 \x01(\x05\x12\x32\n\x06Labels\x18\x05 \x03(\x0b\x32\".Im.Scrm.Ww.Proto.UserLabelMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WUserLabelPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_USERLABELPUSHNOTICEMESSAGE']._serialized_start=67
  _globals['_USERLABELPUSHNOTICEMESSAGE']._serialized_end=219
  _globals['_USERLABELMESSAGE']._serialized_start=221
  _globals['_USERLABELMESSAGE']._serialized_end=302
  _globals['_USERLABELGROUPMESSAGE']._serialized_start=305
  _globals['_USERLABELGROUPMESSAGE']._serialized_end=437
# @@protoc_insertion_point(module_scope)
