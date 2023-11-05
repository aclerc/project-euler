from project_euler.ten_thousand_first_prime import nth_prime


def test_p007() -> None:
    n = 10001
    ans = 104743
    assert nth_prime(n) == ans
