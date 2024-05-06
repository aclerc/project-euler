from project_euler.pandigital_products import sum_pandigital_products


def test_p032() -> None:
    n = 9
    ans = 45228
    assert sum_pandigital_products(n) == ans
