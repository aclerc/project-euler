import math

from project_euler.decorators import print_run_time


@print_run_time
def y_choose_x(y: int, x: int) -> int:
    return math.factorial(y) // math.factorial(y - x) // math.factorial(x)


def count_lattice_routes(grid_side: int) -> int:
    return y_choose_x(2 * grid_side, grid_side)


if __name__ == "__main__":
    grid_side = 20
    print(
        "Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, "
        "there are exactly 6 routes to the bottom right corner.",
    )
    print(f"How many such routes are there in a {grid_side}x{grid_side} grid?")
    print(count_lattice_routes(grid_side))
