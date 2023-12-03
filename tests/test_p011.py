from pathlib import Path

import numpy as np

from project_euler.largest_product_in_a_grid import largest_product_n_adjacent


def test_p011() -> None:
    grid = np.loadtxt(Path(__file__).parents[1] / "input_data" / "p11.txt")
    n = 4
    ans = 70600674
    assert largest_product_n_adjacent(grid, n) == ans
