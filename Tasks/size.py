def size(size: int) -> str:
    converted_size = '0 byte'

    if size != 0:
        exponent = size.bit_length() // 10
        converted_size = calculate_size_from_exp(size, exponent)

    return converted_size


def calculate_size_from_exp(size: int, exponent: int) -> str:
    result = ''

    match exponent:
        case 1:
            result = str(round(size / 1000)) + ' kb'
        case 2:
            result = str(round(size / 1000000)) + ' mb'
        case 3:
            result = str(round(size / 1000000000)) + ' gb'
        case _:
            result = str(size) + ' byte'

    return result
