from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor
EFFECT_ALLOW: Effect
EFFECT_DENY: Effect
EFFECT_NO_MATCH: Effect
EFFECT_UNSPECIFIED: Effect

class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
