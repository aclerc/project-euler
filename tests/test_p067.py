from pathlib import Path

from project_euler.maximum_path_sum import max_path_sum


def test_p067() -> None:
    fpath = Path(__file__).parents[1] / "input_data" / "0067_triangle.txt"
    ans = 7273
    assert max_path_sum(fpath) == ans
