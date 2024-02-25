from project_euler.non_abundant_sums import sum_of_n_which_are_not_sum_of_two_abundants


def test_p023() -> None:
    ans = 4179871
    assert sum_of_n_which_are_not_sum_of_two_abundants() == ans
