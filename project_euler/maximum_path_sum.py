from pathlib import Path

import numpy as np

from project_euler.decorators import print_run_time


def load_triangle_from_txt(fpath: Path) -> list[list[int]]:
    with Path.open(fpath) as f:
        return [[int(x) for x in line.split(" ")] for line in f]


@print_run_time
def max_path_sum(fpath: Path) -> int:
    triangle = load_triangle_from_txt(fpath)
    while len(triangle) > 1:
        last_row_rolling_max = np.maximum(triangle[-1][1:], triangle[-1][:-1])
        triangle[-2] = list(last_row_rolling_max + triangle[-2])
        triangle = triangle[:-1]
    return triangle[0][0]


if __name__ == "__main__":
    fpath = Path(__file__).parents[1] / "input_data" / "0018_triangle.txt"

    print("Find the maximum total from top to bottom of the triangle (problem 18)")
    print(max_path_sum(fpath))

    fpath = Path(__file__).parents[1] / "input_data" / "0067_triangle.txt"
    print("Find the maximum total from top to bottom of the triangle (problem 67)")
    print(max_path_sum(fpath))
