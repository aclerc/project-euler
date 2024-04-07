from project_euler.digit_fifth_powers import sum_numbers_that_are_nth_powers_of_their_digits


def test_p030() -> None:
    n = 5
    ans = 443839
    assert sum_numbers_that_are_nth_powers_of_their_digits(n) == ans
