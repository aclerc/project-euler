from pathlib import Path

import numpy as np


def largest_product(lrg_prod: float, this_prod: float) -> float:
    if this_prod > lrg_prod:
        lrg_prod = this_prod
    return lrg_prod


def largest_product_n_adjacent(grid: np.ndarray, n: int) -> int:
    lrg_prod = 0.0
    for x in range(grid.shape[0]):
        for y in range(grid.shape[1]):
            # try down, right, diagonal
            if y <= (grid.shape[1] - n):
                lrg_prod = largest_product(lrg_prod=lrg_prod, this_prod=grid[x, list(range(y, y + 4))].prod())
            if x <= (grid.shape[0] - n):
                lrg_prod = largest_product(lrg_prod=lrg_prod, this_prod=grid[list(range(x, x + 4)), y].prod())
            if x <= (grid.shape[0] - n) and y <= (grid.shape[1] - n):
                lrg_prod = largest_product(
                    lrg_prod=lrg_prod,
                    this_prod=grid[list(range(x, x + 4)), list(range(y, y + 4))].prod(),
                )
                lrg_prod = largest_product(
                    lrg_prod=lrg_prod,
                    this_prod=grid[list(range(x, x + 4)), list(range(y + 3, y - 1, -1))].prod(),
                )
    return int(lrg_prod)


if __name__ == "__main__":
    grid = np.loadtxt(Path(__file__).parents[1] / "input_data/p11.txt")
    n = 4
    print(
        f"What is the greatest product of {n} adjacent numbers in the same direction "
        "(up, down, left, right, or diagonally)?",
    )
    print(f"answer is {largest_product_n_adjacent(grid,n)}")
