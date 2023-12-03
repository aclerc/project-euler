from project_euler.power_digit_sum import sum_digits_of_2e


def test_p016() -> None:
    exponent = 1000
    ans = 1366
    assert sum_digits_of_2e(exponent) == ans
