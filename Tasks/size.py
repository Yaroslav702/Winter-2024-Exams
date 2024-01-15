KILOBYTE = 1000
MEGABYTE = 1000000
GIGABYTE = 1000000000

def size(size: int) -> str:
    converted_size = '0 byte'

    if size != 0:
        exponent = size.bit_length() // 10
        converted_size = calculate_size_from_exp(size, exponent)

    return converted_size


def calculate_size_from_exp(size: int, exponent: int) -> str:
    result = ''

    size_constants = {
        1: KILOBYTE,
        2: MEGABYTE,
        3: GIGABYTE,
    }

    size_units = ["byte", "kb", "mb", "gb"]

    constant = size_constants.get(exponent, 1) 

    result = f'{round(size / constant)} {size_units[exponent]}'

    return result
