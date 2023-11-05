from project_euler.summation_of_primes import sum_primes_below


def test_p010() -> None:
    limit = 2 * 10**6
    ans = 142913828922
    assert sum_primes_below(limit) == ans
