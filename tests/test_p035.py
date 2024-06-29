from project_euler.circular_primes import count_circular_primes_below


def test_p035() -> None:
    ans = 55
    assert count_circular_primes_below(10**6) == ans
