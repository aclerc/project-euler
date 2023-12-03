from pathlib import Path

from project_euler.maximum_path_sum import max_path_sum


def test_p018() -> None:
    fpath = Path(__file__).parents[1] / "input_data" / "0018_triangle.txt"
    ans = 1074
    assert max_path_sum(fpath) == ans
