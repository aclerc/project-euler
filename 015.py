import math
import time

start = time.time()
grid_side = 20
print(
    "Starting in the top left corner of a 2x2 grid, and only being able to move to the right and down, "
    "there are exactly 6 routes to the bottom right corner."
)
print(f"How many such routes are there in a {grid_side}x{grid_side} grid?")


def y_choose_x(y, x):
    # this approach is way too slow
    if x < 0 or y < 0:
        raise ValueError("x and y must be >= 0")
    elif x > y:
        raise ValueError("x must by <= y")
    elif x == 0 or x == y:
        # print(f"{y} choose {x}")
        return 1
    elif x == 1 or x == (y - 1):
        # print(f"{y} choose {x}")
        return y
    else:
        return y_choose_x(y - 1, x) + y_choose_x(y - 1, x - 1)


def y_choose_x2(y, x):
    return math.factorial(y) // math.factorial(y - x) // math.factorial(x)


knowns = {}


def y_choose_x3(y, x, knowns):
    # approach using memoization
    if x < 0 or y < 0:
        raise ValueError("x and y must be >= 0")
    elif x > y:
        raise ValueError("x must by <= y")
    elif x == 0 or x == y:
        return 1
    elif x == 1 or x == (y - 1):
        return y
    elif knowns.get((y, x), None) is not None:
        return knowns[(y, x)]
    else:
        knowns[(y, x)] = y_choose_x3(y - 1, x, knowns) + y_choose_x3(y - 1, x - 1, knowns)
        return knowns[(y, x)]


answer = y_choose_x2(2 * grid_side, grid_side)

print(f"\nanswer={answer}")
if grid_side == 20:
    assert answer == 137846528820
print(f"time taken = {time.time() - start:.4f}s")
