from project_euler.number_spiral_diagonals import sum_numbers_on_spiral_diagonals


def test_p028() -> None:
    side_len = 1001
    ans = 669171001
    assert sum_numbers_on_spiral_diagonals(side_len) == ans
