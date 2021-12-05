from dataclasses import dataclass
from strenum import StrEnum
from typing import List
from validator import validate_type
from enum_util import is_enum_member, enum_members

PokemonType = StrEnum('PokemonType', [
                      'ELECTRIC', 'GROUND', 'FIRE', 'WATER', 'WIND', 'PSYCHIC', 'GRASS'])


@dataclass(frozen=True)
class Pokemon:
    ''' Pokemon class declares the fields that an elasticsearch document of pokemon should have
        and their expected types
    '''

    pokadex_id: int
    name: str
    nickname: str
    level: int
    type: str
    skills: List[str]

    ID_FIELD_NAME = 'pokadex_id'    # we'll also use this field to be the document id


def validate_pokemon(pokemon_json: dict) -> dict:
    ''' validates the values in the pokemon json are consistent with the
        annotations in Pokemon class, and removes unannotated keys

        Returns: a pokemon json with only fields defined in Pokemon class
        Raises: ValueError on type validation failure
     '''
    annotations = annotations = getattr(Pokemon, '__annotations__', {})
    res = {}
    for field_name, value in pokemon_json.items():
        if field_name not in annotations:
            continue
        expected_type = annotations[field_name]
        if not validate_type(value, expected_type):
            value_type = type(value)
            raise ValueError(f"Field '{field_name}' of type '{_type_name(expected_type)}' cannot "
                             f"be set to '{value}' of type '{_type_name(value_type)}'")
        res[field_name] = value
    _validate_constraints(res)
    return res


def _type_name(t: type) -> str:
    ''' returns the name of the type, or its string representation '''
    return getattr(t, '__name__', None) or getattr(t, '_name', None) or str(t)


def _validate_constraints(pokemon_json: dict) -> None:
    ''' validates constraints on pokemon values
    '''
    level = pokemon_json['level']
    if not level > 0:
        raise ValueError("Field 'level' must greater than zero")
    pokemon_type = pokemon_json['type']
    if not is_enum_member(pokemon_type, PokemonType):
        message = f"Field 'type' cannot be set to '{pokemon_type}', it must be one of {enum_members(PokemonType)}"
        raise ValueError(message)
