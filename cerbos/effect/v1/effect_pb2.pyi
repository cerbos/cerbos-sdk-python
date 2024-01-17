from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from typing import ClassVar as _ClassVar

DESCRIPTOR: _descriptor.FileDescriptor

class Effect(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    EFFECT_UNSPECIFIED: _ClassVar[Effect]
    EFFECT_ALLOW: _ClassVar[Effect]
    EFFECT_DENY: _ClassVar[Effect]
    EFFECT_NO_MATCH: _ClassVar[Effect]
EFFECT_UNSPECIFIED: Effect
EFFECT_ALLOW: Effect
EFFECT_DENY: Effect
EFFECT_NO_MATCH: Effect
