from google.protobuf import duration_pb2 as _duration_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class Constant(_message.Message):
    __slots__ = ["bool_value", "bytes_value", "double_value", "duration_value", "int64_value", "null_value", "string_value", "timestamp_value", "uint64_value"]
    BOOL_VALUE_FIELD_NUMBER: _ClassVar[int]
    BYTES_VALUE_FIELD_NUMBER: _ClassVar[int]
    DOUBLE_VALUE_FIELD_NUMBER: _ClassVar[int]
    DURATION_VALUE_FIELD_NUMBER: _ClassVar[int]
    INT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    NULL_VALUE_FIELD_NUMBER: _ClassVar[int]
    STRING_VALUE_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_VALUE_FIELD_NUMBER: _ClassVar[int]
    UINT64_VALUE_FIELD_NUMBER: _ClassVar[int]
    bool_value: bool
    bytes_value: bytes
    double_value: float
    duration_value: _duration_pb2.Duration
    int64_value: int
    null_value: _struct_pb2.NullValue
    string_value: str
    timestamp_value: _timestamp_pb2.Timestamp
    uint64_value: int
    def __init__(self, null_value: _Optional[_Union[_struct_pb2.NullValue, str]] = ..., bool_value: bool = ..., int64_value: _Optional[int] = ..., uint64_value: _Optional[int] = ..., double_value: _Optional[float] = ..., string_value: _Optional[str] = ..., bytes_value: _Optional[bytes] = ..., duration_value: _Optional[_Union[_duration_pb2.Duration, _Mapping]] = ..., timestamp_value: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ...) -> None: ...

class Expr(_message.Message):
    __slots__ = ["call_expr", "comprehension_expr", "const_expr", "id", "ident_expr", "list_expr", "select_expr", "struct_expr"]
    class Call(_message.Message):
        __slots__ = ["args", "function", "target"]
        ARGS_FIELD_NUMBER: _ClassVar[int]
        FUNCTION_FIELD_NUMBER: _ClassVar[int]
        TARGET_FIELD_NUMBER: _ClassVar[int]
        args: _containers.RepeatedCompositeFieldContainer[Expr]
        function: str
        target: Expr
        def __init__(self, target: _Optional[_Union[Expr, _Mapping]] = ..., function: _Optional[str] = ..., args: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ...) -> None: ...
    class Comprehension(_message.Message):
        __slots__ = ["accu_init", "accu_var", "iter_range", "iter_var", "loop_condition", "loop_step", "result"]
        ACCU_INIT_FIELD_NUMBER: _ClassVar[int]
        ACCU_VAR_FIELD_NUMBER: _ClassVar[int]
        ITER_RANGE_FIELD_NUMBER: _ClassVar[int]
        ITER_VAR_FIELD_NUMBER: _ClassVar[int]
        LOOP_CONDITION_FIELD_NUMBER: _ClassVar[int]
        LOOP_STEP_FIELD_NUMBER: _ClassVar[int]
        RESULT_FIELD_NUMBER: _ClassVar[int]
        accu_init: Expr
        accu_var: str
        iter_range: Expr
        iter_var: str
        loop_condition: Expr
        loop_step: Expr
        result: Expr
        def __init__(self, iter_var: _Optional[str] = ..., iter_range: _Optional[_Union[Expr, _Mapping]] = ..., accu_var: _Optional[str] = ..., accu_init: _Optional[_Union[Expr, _Mapping]] = ..., loop_condition: _Optional[_Union[Expr, _Mapping]] = ..., loop_step: _Optional[_Union[Expr, _Mapping]] = ..., result: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class CreateList(_message.Message):
        __slots__ = ["elements", "optional_indices"]
        ELEMENTS_FIELD_NUMBER: _ClassVar[int]
        OPTIONAL_INDICES_FIELD_NUMBER: _ClassVar[int]
        elements: _containers.RepeatedCompositeFieldContainer[Expr]
        optional_indices: _containers.RepeatedScalarFieldContainer[int]
        def __init__(self, elements: _Optional[_Iterable[_Union[Expr, _Mapping]]] = ..., optional_indices: _Optional[_Iterable[int]] = ...) -> None: ...
    class CreateStruct(_message.Message):
        __slots__ = ["entries", "message_name"]
        class Entry(_message.Message):
            __slots__ = ["field_key", "id", "map_key", "optional_entry", "value"]
            FIELD_KEY_FIELD_NUMBER: _ClassVar[int]
            ID_FIELD_NUMBER: _ClassVar[int]
            MAP_KEY_FIELD_NUMBER: _ClassVar[int]
            OPTIONAL_ENTRY_FIELD_NUMBER: _ClassVar[int]
            VALUE_FIELD_NUMBER: _ClassVar[int]
            field_key: str
            id: int
            map_key: Expr
            optional_entry: bool
            value: Expr
            def __init__(self, id: _Optional[int] = ..., field_key: _Optional[str] = ..., map_key: _Optional[_Union[Expr, _Mapping]] = ..., value: _Optional[_Union[Expr, _Mapping]] = ..., optional_entry: bool = ...) -> None: ...
        ENTRIES_FIELD_NUMBER: _ClassVar[int]
        MESSAGE_NAME_FIELD_NUMBER: _ClassVar[int]
        entries: _containers.RepeatedCompositeFieldContainer[Expr.CreateStruct.Entry]
        message_name: str
        def __init__(self, message_name: _Optional[str] = ..., entries: _Optional[_Iterable[_Union[Expr.CreateStruct.Entry, _Mapping]]] = ...) -> None: ...
    class Ident(_message.Message):
        __slots__ = ["name"]
        NAME_FIELD_NUMBER: _ClassVar[int]
        name: str
        def __init__(self, name: _Optional[str] = ...) -> None: ...
    class Select(_message.Message):
        __slots__ = ["field", "operand", "test_only"]
        FIELD_FIELD_NUMBER: _ClassVar[int]
        OPERAND_FIELD_NUMBER: _ClassVar[int]
        TEST_ONLY_FIELD_NUMBER: _ClassVar[int]
        field: str
        operand: Expr
        test_only: bool
        def __init__(self, operand: _Optional[_Union[Expr, _Mapping]] = ..., field: _Optional[str] = ..., test_only: bool = ...) -> None: ...
    CALL_EXPR_FIELD_NUMBER: _ClassVar[int]
    COMPREHENSION_EXPR_FIELD_NUMBER: _ClassVar[int]
    CONST_EXPR_FIELD_NUMBER: _ClassVar[int]
    IDENT_EXPR_FIELD_NUMBER: _ClassVar[int]
    ID_FIELD_NUMBER: _ClassVar[int]
    LIST_EXPR_FIELD_NUMBER: _ClassVar[int]
    SELECT_EXPR_FIELD_NUMBER: _ClassVar[int]
    STRUCT_EXPR_FIELD_NUMBER: _ClassVar[int]
    call_expr: Expr.Call
    comprehension_expr: Expr.Comprehension
    const_expr: Constant
    id: int
    ident_expr: Expr.Ident
    list_expr: Expr.CreateList
    select_expr: Expr.Select
    struct_expr: Expr.CreateStruct
    def __init__(self, id: _Optional[int] = ..., const_expr: _Optional[_Union[Constant, _Mapping]] = ..., ident_expr: _Optional[_Union[Expr.Ident, _Mapping]] = ..., select_expr: _Optional[_Union[Expr.Select, _Mapping]] = ..., call_expr: _Optional[_Union[Expr.Call, _Mapping]] = ..., list_expr: _Optional[_Union[Expr.CreateList, _Mapping]] = ..., struct_expr: _Optional[_Union[Expr.CreateStruct, _Mapping]] = ..., comprehension_expr: _Optional[_Union[Expr.Comprehension, _Mapping]] = ...) -> None: ...

class ParsedExpr(_message.Message):
    __slots__ = ["expr", "source_info"]
    EXPR_FIELD_NUMBER: _ClassVar[int]
    SOURCE_INFO_FIELD_NUMBER: _ClassVar[int]
    expr: Expr
    source_info: SourceInfo
    def __init__(self, expr: _Optional[_Union[Expr, _Mapping]] = ..., source_info: _Optional[_Union[SourceInfo, _Mapping]] = ...) -> None: ...

class SourceInfo(_message.Message):
    __slots__ = ["line_offsets", "location", "macro_calls", "positions", "syntax_version"]
    class MacroCallsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: Expr
        def __init__(self, key: _Optional[int] = ..., value: _Optional[_Union[Expr, _Mapping]] = ...) -> None: ...
    class PositionsEntry(_message.Message):
        __slots__ = ["key", "value"]
        KEY_FIELD_NUMBER: _ClassVar[int]
        VALUE_FIELD_NUMBER: _ClassVar[int]
        key: int
        value: int
        def __init__(self, key: _Optional[int] = ..., value: _Optional[int] = ...) -> None: ...
    LINE_OFFSETS_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    MACRO_CALLS_FIELD_NUMBER: _ClassVar[int]
    POSITIONS_FIELD_NUMBER: _ClassVar[int]
    SYNTAX_VERSION_FIELD_NUMBER: _ClassVar[int]
    line_offsets: _containers.RepeatedScalarFieldContainer[int]
    location: str
    macro_calls: _containers.MessageMap[int, Expr]
    positions: _containers.ScalarMap[int, int]
    syntax_version: str
    def __init__(self, syntax_version: _Optional[str] = ..., location: _Optional[str] = ..., line_offsets: _Optional[_Iterable[int]] = ..., positions: _Optional[_Mapping[int, int]] = ..., macro_calls: _Optional[_Mapping[int, Expr]] = ...) -> None: ...

class SourcePosition(_message.Message):
    __slots__ = ["column", "line", "location", "offset"]
    COLUMN_FIELD_NUMBER: _ClassVar[int]
    LINE_FIELD_NUMBER: _ClassVar[int]
    LOCATION_FIELD_NUMBER: _ClassVar[int]
    OFFSET_FIELD_NUMBER: _ClassVar[int]
    column: int
    line: int
    location: str
    offset: int
    def __init__(self, location: _Optional[str] = ..., offset: _Optional[int] = ..., line: _Optional[int] = ..., column: _Optional[int] = ...) -> None: ...
