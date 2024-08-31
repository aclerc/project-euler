from project_euler.pandigital_multiples import largest_pandigital_from_concatenated_product


def test_p038() -> None:
    ans = 932718654
    assert largest_pandigital_from_concatenated_product(9) == ans
