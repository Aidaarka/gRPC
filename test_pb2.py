# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: test.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntest.proto\x1a\x1cgoogle/protobuf/struct.proto\"S\n\x0bTestRequest\x12\r\n\x05nrows\x18\x01 \x01(\x05\x12\x10\n\x08\x66ilename\x18\x02 \x01(\t\x12\x0e\n\x06option\x18\x03 \x01(\x05\x12\x13\n\x0b\x63olumn_name\x18\x04 \x01(\t\"5\n\tTestReply\x12(\n\x07message\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct2\xf7\x01\n\x0bTestService\x12\"\n\x04test\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x12%\n\x07\x64\x66_info\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x12\"\n\x04\x64\x61ta\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x12$\n\x06n_rows\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x12(\n\nmax_by_col\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x12)\n\x0bupload_data\x12\x0c.TestRequest\x1a\n.TestReply\"\x00\x62\x06proto3')



_TESTREQUEST = DESCRIPTOR.message_types_by_name['TestRequest']
_TESTREPLY = DESCRIPTOR.message_types_by_name['TestReply']
TestRequest = _reflection.GeneratedProtocolMessageType('TestRequest', (_message.Message,), {
  'DESCRIPTOR' : _TESTREQUEST,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:TestRequest)
  })
_sym_db.RegisterMessage(TestRequest)

TestReply = _reflection.GeneratedProtocolMessageType('TestReply', (_message.Message,), {
  'DESCRIPTOR' : _TESTREPLY,
  '__module__' : 'test_pb2'
  # @@protoc_insertion_point(class_scope:TestReply)
  })
_sym_db.RegisterMessage(TestReply)

_TESTSERVICE = DESCRIPTOR.services_by_name['TestService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TESTREQUEST._serialized_start=44
  _TESTREQUEST._serialized_end=127
  _TESTREPLY._serialized_start=129
  _TESTREPLY._serialized_end=182
  _TESTSERVICE._serialized_start=185
  _TESTSERVICE._serialized_end=432
# @@protoc_insertion_point(module_scope)
