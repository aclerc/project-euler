from project_euler.even_fibonacci_numbers import sum_even_fibonacci_ns


def test_p002() -> None:
    max_n = 4000000 - 1
    ans = 4613732
    assert sum_even_fibonacci_ns(max_n) == ans
