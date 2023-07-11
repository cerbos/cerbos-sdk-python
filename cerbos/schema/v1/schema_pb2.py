# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cerbos/schema/v1/schema.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63\x65rbos/schema/v1/schema.proto\x12\x10\x63\x65rbos.schema.v1\x1a\x1fgoogle/api/field_behavior.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x17validate/validate.proto\"\xce\x01\n\x0fValidationError\x12\x12\n\x04path\x18\x01 \x01(\tR\x04path\x12\x18\n\x07message\x18\x02 \x01(\tR\x07message\x12@\n\x06source\x18\x03 \x01(\x0e\x32(.cerbos.schema.v1.ValidationError.SourceR\x06source\"K\n\x06Source\x12\x16\n\x12SOURCE_UNSPECIFIED\x10\x00\x12\x14\n\x10SOURCE_PRINCIPAL\x10\x01\x12\x13\n\x0fSOURCE_RESOURCE\x10\x02\"\xcb\x01\n\x06Schema\x12U\n\x02id\x18\x01 \x01(\tBE\x92\x41\x34\x32 Unique identifier for the schemaJ\x10\"principal.json\"\xe2\x41\x01\x02\xfa\x42\x07r\x05\x10\x01\x18\xff\x01R\x02id\x12j\n\ndefinition\x18\x02 \x01(\x0c\x42J\x92\x41<2\x16JSON schema definitionJ\"{\"type\":\"object\", \"properties\":{}}\xe2\x41\x01\x02\xfa\x42\x04z\x02\x10\nR\ndefinitionBo\n\x18\x64\x65v.cerbos.api.v1.schemaZ<github.com/cerbos/cerbos/api/genpb/cerbos/schema/v1;schemav1\xaa\x02\x14\x43\x65rbos.Api.V1.Schemab\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cerbos.schema.v1.schema_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030dev.cerbos.api.v1.schemaZ<github.com/cerbos/cerbos/api/genpb/cerbos/schema/v1;schemav1\252\002\024Cerbos.Api.V1.Schema'
  _SCHEMA.fields_by_name['id']._options = None
  _SCHEMA.fields_by_name['id']._serialized_options = b'\222A42 Unique identifier for the schemaJ\020\"principal.json\"\342A\001\002\372B\007r\005\020\001\030\377\001'
  _SCHEMA.fields_by_name['definition']._options = None
  _SCHEMA.fields_by_name['definition']._serialized_options = b'\222A<2\026JSON schema definitionJ\"{\"type\":\"object\", \"properties\":{}}\342A\001\002\372B\004z\002\020\n'
  _globals['_VALIDATIONERROR']._serialized_start=158
  _globals['_VALIDATIONERROR']._serialized_end=364
  _globals['_VALIDATIONERROR_SOURCE']._serialized_start=289
  _globals['_VALIDATIONERROR_SOURCE']._serialized_end=364
  _globals['_SCHEMA']._serialized_start=367
  _globals['_SCHEMA']._serialized_end=570
# @@protoc_insertion_point(module_scope)
