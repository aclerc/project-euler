from project_euler.smallest_multiple import first_evenly_divisible_by_all_up_to_n


def test_q005() -> None:
    n = 20
    ans = 232792560
    assert first_evenly_divisible_by_all_up_to_n(n) == ans
