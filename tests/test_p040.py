from project_euler.champernownes_constant import multiply_champernowne_digits


def test_p040() -> None:
    ans = 210
    assert multiply_champernowne_digits([1, 10, 100, 1000, 10000, 100000, 1000000]) == ans
