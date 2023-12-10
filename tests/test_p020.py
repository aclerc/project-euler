from project_euler.factorial_digit_sum import sum_digits_factorial


def test_p020() -> None:
    ans = 648
    assert sum_digits_factorial(100) == ans
