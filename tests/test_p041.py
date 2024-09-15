from project_euler.pandigital_prime import largest_pandigital_prime


def test_p041() -> None:
    ans = 7652413
    assert largest_pandigital_prime() == ans
