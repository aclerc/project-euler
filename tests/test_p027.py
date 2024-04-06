from project_euler.quadratic_primes import product_coeffs_for_max_quadratic_primes


def test_p027() -> None:
    limit = 1000
    ans = -59231
    assert product_coeffs_for_max_quadratic_primes(limit) == ans
