from project_euler.truncatable_primes import sum_of_all_truncatable_primes


def test_p037() -> None:
    ans = 748317
    assert sum_of_all_truncatable_primes() == ans
