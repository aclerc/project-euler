from project_euler.double_base_palindromes import sum_palindromic_base_10_and_2_less_than


def test_p036() -> None:
    ans = 872187
    assert sum_palindromic_base_10_and_2_less_than(10**6) == ans
