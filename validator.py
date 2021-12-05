def validate_type(value, expected_type):
    if expected_type.__module__ == 'typing':
        return _validate_typing_type(value, expected_type)
    elif expected_type.__module__ == 'builtins':
        return _validate_builtins_type(value, expected_type)
    else:
        return _validate_type_inheritance(value, expected_type)


def _validate_builtins_type(value, expected_type):
    value_type = type(value)
    return value_type is expected_type


def _validate_type_inheritance(value, expected_type):
    value_type = type(value)
    return isinstance(value_type, expected_type)


def _validate_typing_type(value, expected_type):
    value_type = type(value)
    expected_type_origin = getattr(expected_type, '__origin__', None)
    if value_type != expected_type_origin:
        return False
    expected_type_origin_name = getattr(expected_type_origin, '__name__', None)
    if expected_type_origin_name == 'list':
        value_type = expected_type.__args__[0]
        for x in value:
            if not validate_type(x, value_type):
                return False
    else:
        # TODO: complete implementation
        raise NotImplemented(str(expected_type))
    return True
