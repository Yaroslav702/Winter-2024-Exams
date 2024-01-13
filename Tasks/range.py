def _range(Range: tuple) -> list:
    result_range = []
    start_val, stop_val = Range

    if stop_val >= start_val:
        result_range = list(range(start_val, stop_val + 1))

    return result_range