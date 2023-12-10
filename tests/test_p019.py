from project_euler.counting_sundays import count_sundays_on_first_of_month


def test_p019() -> None:
    ans = 171
    assert count_sundays_on_first_of_month(1901, 2000) == ans
