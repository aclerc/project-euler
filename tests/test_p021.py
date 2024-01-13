from project_euler.amicable_numbers import sum_amicable_numbers_under


def test_p021() -> None:
    ans = 31626
    assert sum_amicable_numbers_under(10000) == ans
