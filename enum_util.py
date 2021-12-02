def enum_members(enum_type):
    return [e.value for e in enum_type]


def is_enum_member(member, enum_type):
    return enum_type.__members__.get(member)
