# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: cerbos/engine/v1/engine.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from cerbos.effect.v1 import effect_pb2 as cerbos_dot_effect_dot_v1_dot_effect__pb2
from cerbos.schema.v1 import schema_pb2 as cerbos_dot_schema_dot_v1_dot_schema__pb2
from google.api.expr.v1alpha1 import checked_pb2 as google_dot_api_dot_expr_dot_v1alpha1_dot_checked__pb2
from google.api import field_behavior_pb2 as google_dot_api_dot_field__behavior__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from protoc_gen_openapiv2.options import annotations_pb2 as protoc__gen__openapiv2_dot_options_dot_annotations__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1d\x63\x65rbos/engine/v1/engine.proto\x12\x10\x63\x65rbos.engine.v1\x1a\x1d\x63\x65rbos/effect/v1/effect.proto\x1a\x1d\x63\x65rbos/schema/v1/schema.proto\x1a&google/api/expr/v1alpha1/checked.proto\x1a\x1fgoogle/api/field_behavior.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a.protoc-gen-openapiv2/options/annotations.proto\x1a\x17validate/validate.proto\"\x8b\t\n\x12PlanResourcesInput\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12.\n\tprincipal\x18\x03 \x01(\x0b\x32\x1b.cerbos.engine.v1.Principal\x12?\n\x08resource\x18\x04 \x01(\x0b\x32-.cerbos.engine.v1.PlanResourcesInput.Resource\x12+\n\x08\x61ux_data\x18\x05 \x01(\x0b\x32\x19.cerbos.engine.v1.AuxData\x12\x14\n\x0cinclude_meta\x18\x06 \x01(\x08\x1a\x9c\x07\n\x08Resource\x12\xc2\x01\n\x04kind\x18\x01 \x01(\tB\xb3\x01\x92\x41\x62\x32\x0eResource kind.J\x0e\"album:object\"\x8a\x01?^[[:alpha:]][[:word:]\\@\\.\\-]*(\\:[[:alpha:]][[:word:]\\@\\.\\-]*)*$\xe2\x41\x01\x02\xfa\x42GrE\x10\x01\x32\x41^[[:alpha:]][[:word:]\\@\\.\\-/]*(\\:[[:alpha:]][[:word:]\\@\\.\\-/]*)*$\x12\xb2\x01\n\x04\x61ttr\x18\x02 \x03(\x0b\x32\x37.cerbos.engine.v1.PlanResourcesInput.Resource.AttrEntryBk\x92\x41`2^Key-value pairs of contextual data about the resource that are known at a time of the request.\xfa\x42\x05\x9a\x01\x02\x18\x01\x12\xce\x01\n\x0epolicy_version\x18\x03 \x01(\tB\xb5\x01\x92\x41\x99\x01\x32|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\x8a\x01\r^[[:word:]]*$\xe2\x41\x01\x01\xfa\x42\x11r\x0f\x32\r^[[:word:]]*$\x12\xff\x01\n\x05scope\x18\x04 \x01(\tB\xef\x01\x92\x41\xb1\x01\x32}A dot-separated scope that describes the hierarchy this resource belongs to. This is used for determining policy inheritance.\x8a\x01/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\xe2\x41\x01\x01\xfa\x42\x33r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\x1a\x43\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"\xe7\x03\n\x10PlanResourcesAst\x12;\n\nfilter_ast\x18\x01 \x01(\x0b\x32\'.cerbos.engine.v1.PlanResourcesAst.Node\x1a\x9d\x01\n\x04Node\x12P\n\x11logical_operation\x18\x01 \x01(\x0b\x32\x33.cerbos.engine.v1.PlanResourcesAst.LogicalOperationH\x00\x12;\n\nexpression\x18\x02 \x01(\x0b\x32%.google.api.expr.v1alpha1.CheckedExprH\x00\x42\x06\n\x04node\x1a\xf5\x01\n\x10LogicalOperation\x12N\n\x08operator\x18\x01 \x01(\x0e\x32<.cerbos.engine.v1.PlanResourcesAst.LogicalOperation.Operator\x12\x36\n\x05nodes\x18\x02 \x03(\x0b\x32\'.cerbos.engine.v1.PlanResourcesAst.Node\"Y\n\x08Operator\x12\x18\n\x14OPERATOR_UNSPECIFIED\x10\x00\x12\x10\n\x0cOPERATOR_AND\x10\x01\x12\x0f\n\x0bOPERATOR_OR\x10\x02\x12\x10\n\x0cOPERATOR_NOT\x10\x03\"\xe2\x05\n\x13PlanResourcesFilter\x12\xa7\x01\n\x04kind\x18\x01 \x01(\x0e\x32*.cerbos.engine.v1.PlanResourcesFilter.KindBm\x92\x41j2hFilter kind. Defines whether the given action is always allowed, always denied or allowed conditionally.\x12\x8f\x01\n\tcondition\x18\x02 \x01(\x0b\x32\x38.cerbos.engine.v1.PlanResourcesFilter.Expression.OperandBB\x92\x41?2=Filter condition. Only populated if kind is KIND_CONDITIONAL.\x1a\xa9\x02\n\nExpression\x12\x1f\n\x08operator\x18\x01 \x01(\tB\r\x92\x41\n2\x08Operator\x12J\n\x08operands\x18\x02 \x03(\x0b\x32\x38.cerbos.engine.v1.PlanResourcesFilter.Expression.Operand\x1a\x96\x01\n\x07Operand\x12\'\n\x05value\x18\x01 \x01(\x0b\x32\x16.google.protobuf.ValueH\x00\x12\x46\n\nexpression\x18\x02 \x01(\x0b\x32\x30.cerbos.engine.v1.PlanResourcesFilter.ExpressionH\x00\x12\x12\n\x08variable\x18\x03 \x01(\tH\x00\x42\x06\n\x04node:\x15\x92\x41\x12\n\x10\x32\x0e\x43\x45L expression\"c\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x17\n\x13KIND_ALWAYS_ALLOWED\x10\x01\x12\x16\n\x12KIND_ALWAYS_DENIED\x10\x02\x12\x14\n\x10KIND_CONDITIONAL\x10\x03\"\xf9\x01\n\x13PlanResourcesOutput\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x0e\n\x06\x61\x63tion\x18\x02 \x01(\t\x12\x0c\n\x04kind\x18\x03 \x01(\t\x12\x16\n\x0epolicy_version\x18\x04 \x01(\t\x12\r\n\x05scope\x18\x05 \x01(\t\x12\x35\n\x06\x66ilter\x18\x06 \x01(\x0b\x32%.cerbos.engine.v1.PlanResourcesFilter\x12\x14\n\x0c\x66ilter_debug\x18\x07 \x01(\t\x12<\n\x11validation_errors\x18\x08 \x03(\x0b\x32!.cerbos.schema.v1.ValidationError\"\xec\x01\n\nCheckInput\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12:\n\x08resource\x18\x02 \x01(\x0b\x32\x1a.cerbos.engine.v1.ResourceB\x0c\xe2\x41\x01\x02\xfa\x42\x05\x8a\x01\x02\x10\x01\x12<\n\tprincipal\x18\x03 \x01(\x0b\x32\x1b.cerbos.engine.v1.PrincipalB\x0c\xe2\x41\x01\x02\xfa\x42\x05\x8a\x01\x02\x10\x01\x12#\n\x07\x61\x63tions\x18\x04 \x03(\tB\x12\xe2\x41\x01\x02\xfa\x42\x0b\x92\x01\x08\x18\x01\"\x04r\x02\x10\x01\x12+\n\x08\x61ux_data\x18\x05 \x01(\x0b\x32\x19.cerbos.engine.v1.AuxData\"\xb7\x03\n\x0b\x43heckOutput\x12\x12\n\nrequest_id\x18\x01 \x01(\t\x12\x13\n\x0bresource_id\x18\x02 \x01(\t\x12;\n\x07\x61\x63tions\x18\x03 \x03(\x0b\x32*.cerbos.engine.v1.CheckOutput.ActionsEntry\x12\x1f\n\x17\x65\x66\x66\x65\x63tive_derived_roles\x18\x04 \x03(\t\x12<\n\x11validation_errors\x18\x05 \x03(\x0b\x32!.cerbos.schema.v1.ValidationError\x12.\n\x07outputs\x18\x06 \x03(\x0b\x32\x1d.cerbos.engine.v1.OutputEntry\x1aW\n\x0c\x41\x63tionEffect\x12(\n\x06\x65\x66\x66\x65\x63t\x18\x01 \x01(\x0e\x32\x18.cerbos.effect.v1.Effect\x12\x0e\n\x06policy\x18\x02 \x01(\t\x12\r\n\x05scope\x18\x03 \x01(\t\x1aZ\n\x0c\x41\x63tionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x39\n\x05value\x18\x02 \x01(\x0b\x32*.cerbos.engine.v1.CheckOutput.ActionEffect:\x02\x38\x01\"\xe1\x01\n\x0bOutputEntry\x12`\n\x03src\x18\x01 \x01(\tBS\x92\x41P2)Rule that matched to produce this output.J#\"resource.expense.v1/acme#rule-001\"\x12p\n\x03val\x18\x02 \x01(\x0b\x32\x16.google.protobuf.ValueBK\x92\x41H27Dynamic output, determined by user defined rule output.J\r\"some_string\"\"\x92\x08\n\x08Resource\x12\xdc\x01\n\x04kind\x18\x01 \x01(\tB\xcd\x01\x92\x41|2)Name of the resource kind being accessed.J\r\"album:photo\"\x8a\x01?^[[:alpha:]][[:word:]\\@\\.\\-]*(\\:[[:alpha:]][[:word:]\\@\\.\\-]*)*$\xe2\x41\x01\x02\xfa\x42GrE\x10\x01\x32\x41^[[:alpha:]][[:word:]\\@\\.\\-/]*(\\:[[:alpha:]][[:word:]\\@\\.\\-/]*)*$\x12\xce\x01\n\x0epolicy_version\x18\x02 \x01(\tB\xb5\x01\x92\x41\x99\x01\x32|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\x8a\x01\r^[[:word:]]*$\xe2\x41\x01\x01\xfa\x42\x11r\x0f\x32\r^[[:word:]]*$\x12@\n\x02id\x18\x03 \x01(\tB4\x92\x41&2\x1bID of the resource instanceJ\x07\"XX125\"\xe2\x41\x01\x02\xfa\x42\x04r\x02\x10\x01\x12\xbf\x01\n\x04\x61ttr\x18\x04 \x03(\x0b\x32$.cerbos.engine.v1.Resource.AttrEntryB\x8a\x01\x92\x41\x7f\x32\x64Kay-value pairs of contextual data about this resource that should be used during policy evaluation.J\x17{\"owner\": \"bugs_bunny\"}\xfa\x42\x05\x9a\x01\x02\x18\x01\x12\x8c\x02\n\x05scope\x18\x05 \x01(\tB\xfc\x01\x92\x41\xbe\x01\x32}A dot-separated scope that describes the hierarchy this resource belongs to. This is used for determining policy inheritance.J\x0b\"acme.corp\"\x8a\x01/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\xe2\x41\x01\x01\xfa\x42\x33r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\x1a\x43\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01\"\xb4\x08\n\tPrincipal\x12=\n\x02id\x18\x01 \x01(\tB1\x92\x41#2\x13ID of the principalJ\x0c\"bugs_bunny\"\xe2\x41\x01\x02\xfa\x42\x04r\x02\x10\x01\x12\xce\x01\n\x0epolicy_version\x18\x02 \x01(\tB\xb5\x01\x92\x41\x99\x01\x32|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\x8a\x01\r^[[:word:]]*$\xe2\x41\x01\x01\xfa\x42\x11r\x0f\x32\r^[[:word:]]*$\x12\xa4\x01\n\x05roles\x18\x03 \x03(\tB\x94\x01\x92\x41l2FRoles assigned to this principal from your identity management system.J\x08[\"user\"]\x8a\x01\x11^[[:word:]\\-\\.]+$\xa8\x01\x01\xb0\x01\x01\xe2\x41\x01\x02\xfa\x42\x1e\x92\x01\x1b\x08\x01\x18\x01\"\x15r\x13\x32\x11^[[:word:]\\-\\.]+$\x12\xbf\x01\n\x04\x61ttr\x18\x04 \x03(\x0b\x32%.cerbos.engine.v1.Principal.AttrEntryB\x89\x01\x92\x41~2eKey-value pairs of contextual data about this principal that should be used during policy evaluation.J\x15{\"beta_tester\": true}\xfa\x42\x05\x9a\x01\x02\x18\x01\x12\x8d\x02\n\x05scope\x18\x05 \x01(\tB\xfd\x01\x92\x41\xbf\x01\x32~A dot-separated scope that describes the hierarchy this principal belongs to. This is used for determining policy inheritance.J\x0b\"acme.corp\"\x8a\x01/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\xe2\x41\x01\x01\xfa\x42\x33r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\x1a\x43\n\tAttrEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01:Y\x92\x41V\nT2RA person or application attempting to perform the actions on the set of resources.\"\xa0\x01\n\x07\x41uxData\x12/\n\x03jwt\x18\x01 \x03(\x0b\x32\".cerbos.engine.v1.AuxData.JwtEntry\x1a\x42\n\x08JwtEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12%\n\x05value\x18\x02 \x01(\x0b\x32\x16.google.protobuf.Value:\x02\x38\x01: \x92\x41\x1d\n\x1b\x32\x19Structured auxiliary data\"\xf3\x07\n\x05Trace\x12\x35\n\ncomponents\x18\x01 \x03(\x0b\x32!.cerbos.engine.v1.Trace.Component\x12,\n\x05\x65vent\x18\x02 \x01(\x0b\x32\x1d.cerbos.engine.v1.Trace.Event\x1a\x86\x05\n\tComponent\x12\x34\n\x04kind\x18\x01 \x01(\x0e\x32&.cerbos.engine.v1.Trace.Component.Kind\x12\x10\n\x06\x61\x63tion\x18\x02 \x01(\tH\x00\x12\x16\n\x0c\x64\x65rived_role\x18\x03 \x01(\tH\x00\x12\x0e\n\x04\x65xpr\x18\x04 \x01(\tH\x00\x12\x0f\n\x05index\x18\x05 \x01(\rH\x00\x12\x10\n\x06policy\x18\x06 \x01(\tH\x00\x12\x12\n\x08resource\x18\x07 \x01(\tH\x00\x12\x0e\n\x04rule\x18\x08 \x01(\tH\x00\x12\x0f\n\x05scope\x18\t \x01(\tH\x00\x12>\n\x08variable\x18\n \x01(\x0b\x32*.cerbos.engine.v1.Trace.Component.VariableH\x00\x12\x10\n\x06output\x18\x0b \x01(\tH\x00\x1a&\n\x08Variable\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x0c\n\x04\x65xpr\x18\x02 \x01(\t\"\xab\x02\n\x04Kind\x12\x14\n\x10KIND_UNSPECIFIED\x10\x00\x12\x0f\n\x0bKIND_ACTION\x10\x01\x12\x16\n\x12KIND_CONDITION_ALL\x10\x02\x12\x16\n\x12KIND_CONDITION_ANY\x10\x03\x12\x17\n\x13KIND_CONDITION_NONE\x10\x04\x12\x12\n\x0eKIND_CONDITION\x10\x05\x12\x15\n\x11KIND_DERIVED_ROLE\x10\x06\x12\r\n\tKIND_EXPR\x10\x07\x12\x0f\n\x0bKIND_POLICY\x10\x08\x12\x11\n\rKIND_RESOURCE\x10\t\x12\r\n\tKIND_RULE\x10\n\x12\x0e\n\nKIND_SCOPE\x10\x0b\x12\x11\n\rKIND_VARIABLE\x10\x0c\x12\x12\n\x0eKIND_VARIABLES\x10\r\x12\x0f\n\x0bKIND_OUTPUT\x10\x0e\x42\t\n\x07\x64\x65tails\x1a\xfb\x01\n\x05\x45vent\x12\x34\n\x06status\x18\x01 \x01(\x0e\x32$.cerbos.engine.v1.Trace.Event.Status\x12(\n\x06\x65\x66\x66\x65\x63t\x18\x02 \x01(\x0e\x32\x18.cerbos.effect.v1.Effect\x12\r\n\x05\x65rror\x18\x03 \x01(\t\x12\x0f\n\x07message\x18\x04 \x01(\t\x12&\n\x06result\x18\x05 \x01(\x0b\x32\x16.google.protobuf.Value\"J\n\x06Status\x12\x16\n\x12STATUS_UNSPECIFIED\x10\x00\x12\x14\n\x10STATUS_ACTIVATED\x10\x01\x12\x12\n\x0eSTATUS_SKIPPED\x10\x02\x42o\n\x18\x64\x65v.cerbos.api.v1.engineZ<github.com/cerbos/cerbos/api/genpb/cerbos/engine/v1;enginev1\xaa\x02\x14\x43\x65rbos.Api.V1.Engineb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'cerbos.engine.v1.engine_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\030dev.cerbos.api.v1.engineZ<github.com/cerbos/cerbos/api/genpb/cerbos/engine/v1;enginev1\252\002\024Cerbos.Api.V1.Engine'
  _PLANRESOURCESINPUT_RESOURCE_ATTRENTRY._options = None
  _PLANRESOURCESINPUT_RESOURCE_ATTRENTRY._serialized_options = b'8\001'
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['kind']._options = None
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['kind']._serialized_options = b'\222Ab2\016Resource kind.J\016\"album:object\"\212\001?^[[:alpha:]][[:word:]\\@\\.\\-]*(\\:[[:alpha:]][[:word:]\\@\\.\\-]*)*$\342A\001\002\372BGrE\020\0012A^[[:alpha:]][[:word:]\\@\\.\\-/]*(\\:[[:alpha:]][[:word:]\\@\\.\\-/]*)*$'
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['attr']._options = None
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['attr']._serialized_options = b'\222A`2^Key-value pairs of contextual data about the resource that are known at a time of the request.\372B\005\232\001\002\030\001'
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['policy_version']._options = None
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['policy_version']._serialized_options = b'\222A\231\0012|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\212\001\r^[[:word:]]*$\342A\001\001\372B\021r\0172\r^[[:word:]]*$'
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['scope']._options = None
  _PLANRESOURCESINPUT_RESOURCE.fields_by_name['scope']._serialized_options = b'\222A\261\0012}A dot-separated scope that describes the hierarchy this resource belongs to. This is used for determining policy inheritance.\212\001/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\342A\001\001\372B3r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$'
  _PLANRESOURCESFILTER_EXPRESSION.fields_by_name['operator']._options = None
  _PLANRESOURCESFILTER_EXPRESSION.fields_by_name['operator']._serialized_options = b'\222A\n2\010Operator'
  _PLANRESOURCESFILTER_EXPRESSION._options = None
  _PLANRESOURCESFILTER_EXPRESSION._serialized_options = b'\222A\022\n\0202\016CEL expression'
  _PLANRESOURCESFILTER.fields_by_name['kind']._options = None
  _PLANRESOURCESFILTER.fields_by_name['kind']._serialized_options = b'\222Aj2hFilter kind. Defines whether the given action is always allowed, always denied or allowed conditionally.'
  _PLANRESOURCESFILTER.fields_by_name['condition']._options = None
  _PLANRESOURCESFILTER.fields_by_name['condition']._serialized_options = b'\222A?2=Filter condition. Only populated if kind is KIND_CONDITIONAL.'
  _CHECKINPUT.fields_by_name['resource']._options = None
  _CHECKINPUT.fields_by_name['resource']._serialized_options = b'\342A\001\002\372B\005\212\001\002\020\001'
  _CHECKINPUT.fields_by_name['principal']._options = None
  _CHECKINPUT.fields_by_name['principal']._serialized_options = b'\342A\001\002\372B\005\212\001\002\020\001'
  _CHECKINPUT.fields_by_name['actions']._options = None
  _CHECKINPUT.fields_by_name['actions']._serialized_options = b'\342A\001\002\372B\013\222\001\010\030\001\"\004r\002\020\001'
  _CHECKOUTPUT_ACTIONSENTRY._options = None
  _CHECKOUTPUT_ACTIONSENTRY._serialized_options = b'8\001'
  _OUTPUTENTRY.fields_by_name['src']._options = None
  _OUTPUTENTRY.fields_by_name['src']._serialized_options = b'\222AP2)Rule that matched to produce this output.J#\"resource.expense.v1/acme#rule-001\"'
  _OUTPUTENTRY.fields_by_name['val']._options = None
  _OUTPUTENTRY.fields_by_name['val']._serialized_options = b'\222AH27Dynamic output, determined by user defined rule output.J\r\"some_string\"'
  _RESOURCE_ATTRENTRY._options = None
  _RESOURCE_ATTRENTRY._serialized_options = b'8\001'
  _RESOURCE.fields_by_name['kind']._options = None
  _RESOURCE.fields_by_name['kind']._serialized_options = b'\222A|2)Name of the resource kind being accessed.J\r\"album:photo\"\212\001?^[[:alpha:]][[:word:]\\@\\.\\-]*(\\:[[:alpha:]][[:word:]\\@\\.\\-]*)*$\342A\001\002\372BGrE\020\0012A^[[:alpha:]][[:word:]\\@\\.\\-/]*(\\:[[:alpha:]][[:word:]\\@\\.\\-/]*)*$'
  _RESOURCE.fields_by_name['policy_version']._options = None
  _RESOURCE.fields_by_name['policy_version']._serialized_options = b'\222A\231\0012|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\212\001\r^[[:word:]]*$\342A\001\001\372B\021r\0172\r^[[:word:]]*$'
  _RESOURCE.fields_by_name['id']._options = None
  _RESOURCE.fields_by_name['id']._serialized_options = b'\222A&2\033ID of the resource instanceJ\007\"XX125\"\342A\001\002\372B\004r\002\020\001'
  _RESOURCE.fields_by_name['attr']._options = None
  _RESOURCE.fields_by_name['attr']._serialized_options = b'\222A\1772dKay-value pairs of contextual data about this resource that should be used during policy evaluation.J\027{\"owner\": \"bugs_bunny\"}\372B\005\232\001\002\030\001'
  _RESOURCE.fields_by_name['scope']._options = None
  _RESOURCE.fields_by_name['scope']._serialized_options = b'\222A\276\0012}A dot-separated scope that describes the hierarchy this resource belongs to. This is used for determining policy inheritance.J\013\"acme.corp\"\212\001/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\342A\001\001\372B3r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$'
  _PRINCIPAL_ATTRENTRY._options = None
  _PRINCIPAL_ATTRENTRY._serialized_options = b'8\001'
  _PRINCIPAL.fields_by_name['id']._options = None
  _PRINCIPAL.fields_by_name['id']._serialized_options = b'\222A#2\023ID of the principalJ\014\"bugs_bunny\"\342A\001\002\372B\004r\002\020\001'
  _PRINCIPAL.fields_by_name['policy_version']._options = None
  _PRINCIPAL.fields_by_name['policy_version']._serialized_options = b'\222A\231\0012|The policy version to use to evaluate this request. If not specified, will default to the server-configured default version.J\t\"default\"\212\001\r^[[:word:]]*$\342A\001\001\372B\021r\0172\r^[[:word:]]*$'
  _PRINCIPAL.fields_by_name['roles']._options = None
  _PRINCIPAL.fields_by_name['roles']._serialized_options = b'\222Al2FRoles assigned to this principal from your identity management system.J\010[\"user\"]\212\001\021^[[:word:]\\-\\.]+$\250\001\001\260\001\001\342A\001\002\372B\036\222\001\033\010\001\030\001\"\025r\0232\021^[[:word:]\\-\\.]+$'
  _PRINCIPAL.fields_by_name['attr']._options = None
  _PRINCIPAL.fields_by_name['attr']._serialized_options = b'\222A~2eKey-value pairs of contextual data about this principal that should be used during policy evaluation.J\025{\"beta_tester\": true}\372B\005\232\001\002\030\001'
  _PRINCIPAL.fields_by_name['scope']._options = None
  _PRINCIPAL.fields_by_name['scope']._serialized_options = b'\222A\277\0012~A dot-separated scope that describes the hierarchy this principal belongs to. This is used for determining policy inheritance.J\013\"acme.corp\"\212\001/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$\342A\001\001\372B3r12/^([[:alnum:]][[:word:]\\-]*(\\.[[:word:]\\-]*)*)*$'
  _PRINCIPAL._options = None
  _PRINCIPAL._serialized_options = b'\222AV\nT2RA person or application attempting to perform the actions on the set of resources.'
  _AUXDATA_JWTENTRY._options = None
  _AUXDATA_JWTENTRY._serialized_options = b'8\001'
  _AUXDATA._options = None
  _AUXDATA._serialized_options = b'\222A\035\n\0332\031Structured auxiliary data'
  _globals['_PLANRESOURCESINPUT']._serialized_start=290
  _globals['_PLANRESOURCESINPUT']._serialized_end=1453
  _globals['_PLANRESOURCESINPUT_RESOURCE']._serialized_start=529
  _globals['_PLANRESOURCESINPUT_RESOURCE']._serialized_end=1453
  _globals['_PLANRESOURCESINPUT_RESOURCE_ATTRENTRY']._serialized_start=1386
  _globals['_PLANRESOURCESINPUT_RESOURCE_ATTRENTRY']._serialized_end=1453
  _globals['_PLANRESOURCESAST']._serialized_start=1456
  _globals['_PLANRESOURCESAST']._serialized_end=1943
  _globals['_PLANRESOURCESAST_NODE']._serialized_start=1538
  _globals['_PLANRESOURCESAST_NODE']._serialized_end=1695
  _globals['_PLANRESOURCESAST_LOGICALOPERATION']._serialized_start=1698
  _globals['_PLANRESOURCESAST_LOGICALOPERATION']._serialized_end=1943
  _globals['_PLANRESOURCESAST_LOGICALOPERATION_OPERATOR']._serialized_start=1854
  _globals['_PLANRESOURCESAST_LOGICALOPERATION_OPERATOR']._serialized_end=1943
  _globals['_PLANRESOURCESFILTER']._serialized_start=1946
  _globals['_PLANRESOURCESFILTER']._serialized_end=2684
  _globals['_PLANRESOURCESFILTER_EXPRESSION']._serialized_start=2286
  _globals['_PLANRESOURCESFILTER_EXPRESSION']._serialized_end=2583
  _globals['_PLANRESOURCESFILTER_EXPRESSION_OPERAND']._serialized_start=2410
  _globals['_PLANRESOURCESFILTER_EXPRESSION_OPERAND']._serialized_end=2560
  _globals['_PLANRESOURCESFILTER_KIND']._serialized_start=2585
  _globals['_PLANRESOURCESFILTER_KIND']._serialized_end=2684
  _globals['_PLANRESOURCESOUTPUT']._serialized_start=2687
  _globals['_PLANRESOURCESOUTPUT']._serialized_end=2936
  _globals['_CHECKINPUT']._serialized_start=2939
  _globals['_CHECKINPUT']._serialized_end=3175
  _globals['_CHECKOUTPUT']._serialized_start=3178
  _globals['_CHECKOUTPUT']._serialized_end=3617
  _globals['_CHECKOUTPUT_ACTIONEFFECT']._serialized_start=3438
  _globals['_CHECKOUTPUT_ACTIONEFFECT']._serialized_end=3525
  _globals['_CHECKOUTPUT_ACTIONSENTRY']._serialized_start=3527
  _globals['_CHECKOUTPUT_ACTIONSENTRY']._serialized_end=3617
  _globals['_OUTPUTENTRY']._serialized_start=3620
  _globals['_OUTPUTENTRY']._serialized_end=3845
  _globals['_RESOURCE']._serialized_start=3848
  _globals['_RESOURCE']._serialized_end=4890
  _globals['_RESOURCE_ATTRENTRY']._serialized_start=1386
  _globals['_RESOURCE_ATTRENTRY']._serialized_end=1453
  _globals['_PRINCIPAL']._serialized_start=4893
  _globals['_PRINCIPAL']._serialized_end=5969
  _globals['_PRINCIPAL_ATTRENTRY']._serialized_start=1386
  _globals['_PRINCIPAL_ATTRENTRY']._serialized_end=1453
  _globals['_AUXDATA']._serialized_start=5972
  _globals['_AUXDATA']._serialized_end=6132
  _globals['_AUXDATA_JWTENTRY']._serialized_start=6032
  _globals['_AUXDATA_JWTENTRY']._serialized_end=6098
  _globals['_TRACE']._serialized_start=6135
  _globals['_TRACE']._serialized_end=7146
  _globals['_TRACE_COMPONENT']._serialized_start=6246
  _globals['_TRACE_COMPONENT']._serialized_end=6892
  _globals['_TRACE_COMPONENT_VARIABLE']._serialized_start=6541
  _globals['_TRACE_COMPONENT_VARIABLE']._serialized_end=6579
  _globals['_TRACE_COMPONENT_KIND']._serialized_start=6582
  _globals['_TRACE_COMPONENT_KIND']._serialized_end=6881
  _globals['_TRACE_EVENT']._serialized_start=6895
  _globals['_TRACE_EVENT']._serialized_end=7146
  _globals['_TRACE_EVENT_STATUS']._serialized_start=7072
  _globals['_TRACE_EVENT_STATUS']._serialized_end=7146
# @@protoc_insertion_point(module_scope)
