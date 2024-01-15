def get_range(range_borders: tuple) -> list:
    result_range = []
    start_val, stop_val = range_borders

    if stop_val >= start_val:
        result_range = list(range(start_val, stop_val + 1))

    return result_range
