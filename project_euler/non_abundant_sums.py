import numpy as np
import numpy.typing as npt

from project_euler.decorators import print_run_time


@print_run_time
def get_abundant_array(limit: int) -> npt.NDArray[np.int_]:
    proper_divisor_sum = np.ones(limit, dtype=int)  # all numbers have 1 as a proper divisor
    for k in range(2, limit // 2 + 1):
        proper_divisor_sum[2 * k :: k] += k
    abundant_list = []
    for i, s in enumerate(proper_divisor_sum):
        if s > i:
            abundant_list.append(i)
    del abundant_list[0]  # first entry is 0 which is not an abundant number
    return np.array(abundant_list, dtype=int)


@print_run_time
def sum_of_n_which_are_not_sum_of_two_abundants() -> int:
    # Given: by mathematical analysis, it can be shown that all integers greater than 28123
    # can be written as the sum of two abundant numbers.

    abundant_search_limit = 28124

    abundant_array = get_abundant_array(abundant_search_limit)

    # sieve approach to find all numbers that are not the sum of two abundant numbers
    nums_not_sum_of_two_abundants = np.array(list(range(abundant_search_limit)))
    for i, k in enumerate(abundant_array):
        x = k + abundant_array[i:]  # valid sums of two abundant numbers
        nums_not_sum_of_two_abundants[x[x < abundant_search_limit]] = 0

    return sum(nums_not_sum_of_two_abundants)


if __name__ == "__main__":
    print("Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.")
    print(sum_of_n_which_are_not_sum_of_two_abundants())
