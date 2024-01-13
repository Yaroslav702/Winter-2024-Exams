def count_types(l: list) -> dict:
    types_count = {
        'int': 0,
        'str': 0,
        'bool': 0
    }

    for element in l:
        element_type = type(element).__name__
        types_count[element_type] += 1

    return types_count



