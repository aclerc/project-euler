from pathlib import Path

from project_euler.names_scores import score_names_file


def test_p022() -> None:
    fpath = Path(__file__).parents[1] / "input_data" / "0022_names.txt"
    ans = 871198282
    assert score_names_file(fpath) == ans
