def is_pandigital(x: int) -> bool:
    str_x = str(x)
    n_digits = len(str_x)
    if n_digits > 9:  # noqa PLR2004
        return False
    return "".join(sorted(str_x)) == "".join([str(x + 1) for x in range(n_digits)])
