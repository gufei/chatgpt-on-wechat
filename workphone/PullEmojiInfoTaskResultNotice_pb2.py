# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: PullEmojiInfoTaskResultNotice.proto
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
    'PullEmojiInfoTaskResultNotice.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n#PullEmojiInfoTaskResultNotice.proto\x12\x17Jubo.JuLiao.IM.Wx.Proto\"\x8f\x02\n\x0c\x45mojiMessage\x12\x0b\n\x03md5\x18\x01 \x01(\t\x12\x0e\n\x06\x63\x64nUrl\x18\x02 \x01(\t\x12\x0f\n\x07\x63\x61talog\x18\x03 \x01(\x05\x12\x0c\n\x04type\x18\x04 \x01(\x05\x12\r\n\x05state\x18\x05 \x01(\x05\x12\r\n\x05width\x18\x06 \x01(\x05\x12\x0e\n\x06height\x18\x07 \x01(\x05\x12\x0c\n\x04size\x18\x08 \x01(\x05\x12\x12\n\nencrypturl\x18\n \x01(\t\x12\x0e\n\x06\x61\x65skey\x18\x0b \x01(\t\x12\x11\n\texternUrl\x18\x0c \x01(\t\x12\x11\n\texternMd5\x18\r \x01(\t\x12\x0c\n\x04name\x18\x0e \x01(\t\x12\x0f\n\x07groupId\x18\x0f \x01(\t\x12\x10\n\x08thumbUrl\x18\x10 \x01(\t\x12\x0c\n\x04\x64\x65sc\x18\x11 \x01(\t\"\x7f\n$PullEmojiInfoTaskResultNoticeMessage\x12\x10\n\x08WeChatId\x18\x01 \x01(\t\x12\x0e\n\x06TaskId\x18\x02 \x01(\x03\x12\x35\n\x06\x45mojis\x18\x03 \x03(\x0b\x32%.Jubo.JuLiao.IM.Wx.Proto.EmojiMessageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'PullEmojiInfoTaskResultNotice_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_EMOJIMESSAGE']._serialized_start=65
  _globals['_EMOJIMESSAGE']._serialized_end=336
  _globals['_PULLEMOJIINFOTASKRESULTNOTICEMESSAGE']._serialized_start=338
  _globals['_PULLEMOJIINFOTASKRESULTNOTICEMESSAGE']._serialized_end=465
# @@protoc_insertion_point(module_scope)