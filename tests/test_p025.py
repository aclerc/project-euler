from project_euler.one_thousand_digit_fibonacci_number import index_first_fibonacci_with_n_digits


def test_p025() -> None:
    n = 1000
    ans = 4782
    assert index_first_fibonacci_with_n_digits(n) == ans
