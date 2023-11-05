from project_euler.special_pythagorean_triplet import product_pythagorean_triplet_of_sum


def test_q009() -> None:
    s = 1000
    ans = 31875000
    assert product_pythagorean_triplet_of_sum(s) == ans
