from dataclasses import dataclass
from strenum import StrEnum
from typing import List
from validator import register_setattr_validator
from enum_util import is_enum_member, enum_members
import json

PokemonType = StrEnum('PokemonType', [
                      'ELECTRIC', 'GROUND', 'FIRE', 'WATER', 'WIND', 'PSYCHIC', 'GRASS'])


@dataclass(frozen=True)
class Pokemon:
    name: str
    nickname: str
    level: int
    type: str
    skills: List[str]

    def __init__(self, **kwargs):
        super().__init__()
        annotations = getattr(self, '__annotations__', {})
        setter = register_setattr_validator(self, annotations)
        for k, v in kwargs.items():
            setter(self, k, v)
        self._validate_field_value_constraints()

    def asdict(self):
        return json.dumps({k: getattr(self, k) for k in self.__dataclass_fields__.keys()})

    def _validate_field_value_constraints(self):
        if not self.level > 0:
            raise ValueError("Field 'level' must greater than zero")
        if not is_enum_member(self.type, PokemonType):
            message = f"Field 'type' cannot be set to '{self.type}', it must be one of {enum_members(PokemonType)}"
            raise ValueError(message)
