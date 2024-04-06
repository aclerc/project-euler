
from project_euler.decorators import print_run_time


@print_run_time
def sum_numbers_on_spiral_diagonals(side_len: int) -> int:
    n = 1
    ans = n
    side_len_completed = 1
    while side_len_completed < side_len:
        step = side_len_completed + 1
        for _ in range(4):
            n += step
            ans += n
        side_len_completed += 2
    return ans


if __name__ == "__main__":
    print(
        "It can be verified that the sum of the numbers on the diagonals of a 5x5 sprial is 101. "
        "What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?"
    )
    side_len = 1001
    print(sum_numbers_on_spiral_diagonals(side_len))
