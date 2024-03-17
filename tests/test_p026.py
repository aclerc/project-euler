from project_euler.reciprocal_cycles import d_with_longest_recurring_decimal_cycle


def test_p026() -> None:
    d_limit = 999
    ans = 983
    assert d_with_longest_recurring_decimal_cycle(d_limit) == ans
