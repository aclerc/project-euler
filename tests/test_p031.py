from project_euler.coin_sums import count_ways_to_make_pence


def test_p031() -> None:
    pence_to_make = 2 * 100
    ans = 73682
    assert count_ways_to_make_pence(pence_to_make) == ans
    pence_to_make = 100 * 100
    ans = 1133873304647601  # answer as per overview pdf
    assert count_ways_to_make_pence(pence_to_make) == ans
