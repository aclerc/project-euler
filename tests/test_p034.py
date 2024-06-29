from project_euler.digit_factorials import sum_of_numbers_equal_to_sum_of_factorial_of_their_digits


def test_p034() -> None:
    ans = 40730
    assert sum_of_numbers_equal_to_sum_of_factorial_of_their_digits() == ans
