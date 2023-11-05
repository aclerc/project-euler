from project_euler.multiple_of_3_or_5 import sum_of_two_multiples_below_n


def test_p001() -> None:
    n = 1000
    m1 = 3
    m2 = 5
    ans = 233168
    assert sum_of_two_multiples_below_n(n, m1, m2) == ans
