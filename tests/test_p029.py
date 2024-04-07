from project_euler.distinct_powers import distinct_powers_a_b


def test_p029() -> None:
    limit = 100
    ans = 9183
    assert distinct_powers_a_b(limit) == ans
