from project_euler.number_letter_counts import count_letters_to


def test_p017() -> None:
    n = 1000
    ans = 21124
    assert count_letters_to(n) == ans
