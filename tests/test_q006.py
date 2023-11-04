from project_euler.sum_square_difference import sum_of_squares_minus_square_of_sum


def test_q006() -> None:
    n = 100
    ans = 25164150
    assert sum_of_squares_minus_square_of_sum(n) == ans
