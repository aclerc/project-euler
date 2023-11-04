from project_euler.largest_prime_factor import largest_prime_factor


def test_q003() -> None:
    n = 600851475143
    ans = 6857
    assert largest_prime_factor(n) == ans
