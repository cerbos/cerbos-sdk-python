from google.api.expr.v1alpha1 import syntax_pb2 as _syntax_pb2
from google.protobuf import empty_pb2 as _empty_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class CheckedExpr(_message.Message):
    __slots__ = ["expr", "expr_version", "reference_map", "source_info", "type_map"]
    class ReferenceMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Reference
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Reference, _Mapping]] = ...) -> None: ...
    class TypeMapEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Type
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    EXPR_FIELD_NUMBER: _ClassVar[int]
    EXPR_VERSION_FIELD_NUMBER: _ClassVar[int]
    REFERENCE_MAP_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    TYPE_MAP_FIELD_NUMBER: _ClassVar[int]
    expr: _syntax_pb2.Expr
    expr_version: str
    reference_map: _containers.MessageMap[int, Reference]
    source_info: _syntax_pb2.SourceInfo
    type_map: _containers.MessageMap[int, Type]
    def __init__(self, reference_map: _Optional[_Mapping[int, Reference]] = ..., type_map: _Optional[_Mapping[int, Type]] = ..., source_info: _Optional[_Union[_syntax_pb2.SourceInfo, _Mapping]] = ..., expr_version: _Optional[str] = ..., expr: _Optional[_Union[_syntax_pb2.Expr, _Mapping]] = ...) -> None: ...

class Decl(_message.Message):
    __slots__ = ["function", "ident", "name"]
    class FunctionDecl(_message.Message):
        __slots__ = ["overloads"]
        class Overload(_message.Message):
            __slots__ = ["doc", "is_instance_function", "overload_id", "params", "result_type", "type_params"]
            DOC_FIELD_NUMBER: _ClassVar[int]
            IS_INSTANCE_FUNCTION_FIELD_NUMBER: _ClassVar[int]
            OVERLOAD_ID_FIELD_NUMBER: _ClassVar[int]
            PARAMS_FIELD_NUMBER: _ClassVar[int]
            RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
            TYPE_PARAMS_FIELD_NUMBER: _ClassVar[int]
            doc: str
            is_instance_function: bool
            overload_id: str
            params: _containers.RepeatedCompositeFieldContainer[Type]
            result_type: Type
            type_params: _containers.RepeatedScalarFieldContainer[str]
            def __init__(self, overload_id: _Optional[str] = ..., params: _Optional[_Iterable[_Union[Type, _Mapping]]] = ..., type_params: _Optional[_Iterable[str]] = ..., result_type: _Optional[_Union[Type, _Mapping]] = ..., is_instance_function: bool = ..., doc: _Optional[str] = ...) -> None: ...
        OVERLOADS_FIELD_NUMBER: _ClassVar[int]
        overloads: _containers.RepeatedCompositeFieldContainer[Decl.FunctionDecl.Overload]
        def __init__(self, overloads: _Optional[_Iterable[_Union[Decl.FunctionDecl.Overload, _Mapping]]] = ...) -> None: ...
    class IdentDecl(_message.Message):
        __slots__ = ["doc", "type", "value"]
        DOC_FIELD_NUMBER: _ClassVar[int]
        TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        doc: str
        type: Type
        value: _syntax_pb2.Constant
        def __init__(self, type: _Optional[_Union[Type, _Mapping]] = ..., value: _Optional[_Union[_syntax_pb2.Constant, _Mapping]] = ..., doc: _Optional[str] = ...) -> None: ...
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    IDENT_FIELD_NUMBER: _ClassVar[int]
    NAME_FIELD_NUMBER: _ClassVar[int]
    function: Decl.FunctionDecl
    ident: Decl.IdentDecl
    name: str
    def __init__(self, name: _Optional[str] = ..., ident: _Optional[_Union[Decl.IdentDecl, _Mapping]] = ..., function: _Optional[_Union[Decl.FunctionDecl, _Mapping]] = ...) -> None: ...

class Reference(_message.Message):
    __slots__ = ["name", "overload_id", "value"]
    NAME_FIELD_NUMBER: _ClassVar[int]
    OVERLOAD_ID_FIELD_NUMBER: _ClassVar[int]
    VALUE_FIELD_NUMBER: _ClassVar[int]
    name: str
    overload_id: _containers.RepeatedScalarFieldContainer[str]
    value: _syntax_pb2.Constant
    def __init__(self, name: _Optional[str] = ..., overload_id: _Optional[_Iterable[str]] = ..., value: _Optional[_Union[_syntax_pb2.Constant, _Mapping]] = ...) -> None: ...

class Type(_message.Message):
    __slots__ = ["abstract_type", "dyn", "error", "function", "list_type", "map_type", "message_type", "null", "primitive", "type", "type_param", "well_known", "wrapper"]
    class PrimitiveType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class WellKnownType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
        __slots__ = []
    class AbstractType(_message.Message):
        __slots__ = ["name", "parameter_types"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        PARAMETER_TYPES_FIELD_NUMBER: _ClassVar[int]
        name: str
        parameter_types: _containers.RepeatedCompositeFieldContainer[Type]
        def __init__(self, name: _Optional[str] = ..., parameter_types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class FunctionType(_message.Message):
        __slots__ = ["arg_types", "result_type"]
        ARG_TYPES_FIELD_NUMBER: _ClassVar[int]
        RESULT_TYPE_FIELD_NUMBER: _ClassVar[int]
        arg_types: _containers.RepeatedCompositeFieldContainer[Type]
        result_type: Type
        def __init__(self, result_type: _Optional[_Union[Type, _Mapping]] = ..., arg_types: _Optional[_Iterable[_Union[Type, _Mapping]]] = ...) -> None: ...
    class ListType(_message.Message):
        __slots__ = ["elem_type"]
        ELEM_TYPE_FIELD_NUMBER: _ClassVar[int]
        elem_type: Type
        def __init__(self, elem_type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    class MapType(_message.Message):
        __slots__ = ["key_type", "value_type"]
        KEY_TYPE_FIELD_NUMBER: _ClassVar[int]
        VALUE_TYPE_FIELD_NUMBER: _ClassVar[int]
        key_type: Type
        value_type: Type
        def __init__(self, key_type: _Optional[_Union[Type, _Mapping]] = ..., value_type: _Optional[_Union[Type, _Mapping]] = ...) -> None: ...
    ABSTRACT_TYPE_FIELD_NUMBER: _ClassVar[int]
    ANY: Type.WellKnownType
    BOOL: Type.PrimitiveType
    BYTES: Type.PrimitiveType
    DOUBLE: Type.PrimitiveType
    DURATION: Type.WellKnownType
    DYN_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    FUNCTION_FIELD_NUMBER: _ClassVar[int]
    INT64: Type.PrimitiveType
    LIST_TYPE_FIELD_NUMBER: _ClassVar[int]
    MAP_TYPE_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_TYPE_FIELD_NUMBER: _ClassVar[int]
    NULL_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_FIELD_NUMBER: _ClassVar[int]
    PRIMITIVE_TYPE_UNSPECIFIED: Type.PrimitiveType
    STRING: Type.PrimitiveType
    TIMESTAMP: Type.WellKnownType
    TYPE_FIELD_NUMBER: _ClassVar[int]
    TYPE_PARAM_FIELD_NUMBER: _ClassVar[int]
    UINT64: Type.PrimitiveType
    WELL_KNOWN_FIELD_NUMBER: _ClassVar[int]
    WELL_KNOWN_TYPE_UNSPECIFIED: Type.WellKnownType
    WRAPPER_FIELD_NUMBER: _ClassVar[int]
    abstract_type: Type.AbstractType
    dyn: _empty_pb2.Empty
    error: _empty_pb2.Empty
    function: Type.FunctionType
    list_type: Type.ListType
    map_type: Type.MapType
    message_type: str
    null: _struct_pb2.NullValue
    primitive: Type.PrimitiveType
    type: Type
    type_param: str
    well_known: Type.WellKnownType
    wrapper: Type.PrimitiveType
    def __init__(self, dyn: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., null: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., primitive: _Optional[_Union[Type.PrimitiveType, str]] = ..., wrapper: _Optional[_Union[Type.PrimitiveType, str]] = ..., well_known: _Optional[_Union[Type.WellKnownType, str]] = ..., list_type: _Optional[_Union[Type.ListType, _Mapping]] = ..., map_type: _Optional[_Union[Type.MapType, _Mapping]] = ..., function: _Optional[_Union[Type.FunctionType, _Mapping]] = ..., message_type: _Optional[str] = ..., type_param: _Optional[str] = ..., type: _Optional[_Union[Type, _Mapping]] = ..., error: _Optional[_Union[_empty_pb2.Empty, _Mapping]] = ..., abstract_type: _Optional[_Union[Type.AbstractType, _Mapping]] = ...) -> None: ...
