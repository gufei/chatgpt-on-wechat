# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: GetWeChatsRsp.proto
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
    'GetWeChatsRsp.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import TransportMessage_pb2 as TransportMessage__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13GetWeChatsRsp.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\x1a\x16TransportMessage.proto\"\xa1\x03\n\x10WeChatRspMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x10\n\x08WeChatNo\x18\x02 \x01(\t\x12\x12\n\nWeChatNick\x18\x03 \x01(\t\x12\x0e\n\x06\x41vatar\x18\x04 \x01(\t\x12\x0f\n\x07\x43ountry\x18\x05 \x01(\t\x12\x10\n\x08Province\x18\x06 \x01(\t\x12\x0c\n\x04\x43ity\x18\x07 \x01(\t\x12\x33\n\x06Gender\x18\x08 \x01(\x0e\x32#.Jubo.JuLiao.IM.Wx.Proto.EnumGender\x12\x10\n\x08IsOnline\x18\t \x01(\x08\x12\x11\n\tIsLogined\x18\n \x01(\x08\x12\x10\n\x08IsDelete\x18\x0b \x01(\x08\x12\x11\n\tLoginTime\x18\x0c \x01(\x03\x12\x12\n\nModifyTime\x18\r \x01(\x03\x12\x12\n\nDeviceName\x18\x0e \x01(\t\x12\x14\n\x0cLoginUnionId\x18\x0f \x01(\x03\x12\x42\n\x10LoginAccountType\x18\x10 \x01(\x0e\x32(.Jubo.JuLiao.IM.Wx.Proto.EnumAccountType\x12\x13\n\x0bIsUpgrading\x18\x11 \x01(\x08\"\xb6\x01\n\x14GetWeChatsRspMessage\x12\x0f\n\x07UnionId\x18\x01 \x01(\x03\x12=\n\x0b\x41\x63\x63ountType\x18\x02 \x01(\x0e\x32(.Jubo.JuLiao.IM.Wx.Proto.EnumAccountType\x12\x12\n\nSupplierId\x18\x03 \x01(\x03\x12:\n\x07WeChats\x18\x04 \x03(\x0b\x32).Jubo.JuLiao.IM.Wx.Proto.WeChatRspMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'GetWeChatsRsp_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_WECHATRSPMESSAGE']._serialized_start=73
  _globals['_WECHATRSPMESSAGE']._serialized_end=490
  _globals['_GETWECHATSRSPMESSAGE']._serialized_start=493
  _globals['_GETWECHATSRSPMESSAGE']._serialized_end=675
# @@protoc_insertion_point(module_scope)
