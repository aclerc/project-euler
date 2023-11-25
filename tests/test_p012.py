from project_euler.highly_divisible_triangular_number import first_triangle_number_with_min_divisors


def test_p012() -> None:
    min_num_divisors = 500 + 1
    ans = 76576500
    assert first_triangle_number_with_min_divisors(min_num_divisors) == ans
