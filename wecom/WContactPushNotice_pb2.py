# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: WContactPushNotice.proto
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
    'WContactPushNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import WTransport_pb2 as WTransport__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x18WContactPushNotice.proto\x12\x10Im.Scrm.Ww.Proto\x1a\x10WTransport.proto\"\x97\x01\n\x18\x43ontactPushNoticeMessage\x12\x0c\n\x04WxId\x18\x01 \x01(\x03\x12\x32\n\x08\x43ontacts\x18\x02 \x03(\x0b\x32 .Im.Scrm.Ww.Proto.ContactMessage\x12\x0c\n\x04Size\x18\x03 \x01(\x05\x12\r\n\x05\x43ount\x18\x04 \x01(\x05\x12\x0c\n\x04Page\x18\x05 \x01(\x05\x12\x0e\n\x06TaskId\x18\x06 \x01(\x03\"\xdc\x01\n\x0e\x43ontactMessage\x12\x10\n\x08RemoteId\x18\x01 \x01(\x03\x12\x0e\n\x06\x41\x63\x63tId\x18\x02 \x01(\t\x12\x0c\n\x04Name\x18\x03 \x01(\t\x12\r\n\x05\x41lias\x18\x04 \x01(\t\x12\x0e\n\x06\x41vatar\x18\x05 \x01(\t\x12\x0b\n\x03Job\x18\x06 \x01(\t\x12\x0e\n\x06Mobile\x18\x07 \x01(\t\x12\x0f\n\x07UnionId\x18\x08 \x01(\t\x12,\n\x06Gender\x18\t \x01(\x0e\x32\x1c.Im.Scrm.Ww.Proto.EnumGender\x12\x11\n\tDepartIds\x18\n \x03(\x03\x12\x0c\n\x04\x41ttr\x18\x0b \x01(\x03\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'WContactPushNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_CONTACTPUSHNOTICEMESSAGE']._serialized_start=65
  _globals['_CONTACTPUSHNOTICEMESSAGE']._serialized_end=216
  _globals['_CONTACTMESSAGE']._serialized_start=219
  _globals['_CONTACTMESSAGE']._serialized_end=439
# @@protoc_insertion_point(module_scope)
