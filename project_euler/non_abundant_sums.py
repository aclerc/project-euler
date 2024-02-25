import math

import numpy as np
import numpy.typing as npt

from project_euler.decorators import print_run_time
from project_euler.divisors import largest_prime_factor_upper_bound, proper_divisors_array
from project_euler.list_primes import primes_array_below


def is_abundant(n: int, primes_array: np.ndarray) -> bool:
    return n < sum(proper_divisors_array(n, primes_array))


@print_run_time
def get_abundant_array(limit: int, primes_array: npt.NDArray[np.int_]) -> npt.NDArray[np.int_]:
    abundant_list = [x for x in range(1, limit) if is_abundant(x, primes_array)]
    return np.array(abundant_list)


def is_sum_of_two_abundant_numbers(n: int, abundant_array: npt.NDArray[np.int_]) -> bool:
    # by inspection if n is even and > 46 then ans = True
    # this makes sense because abundant_array is nearly entirely even numbers
    if (n % 2 == 0) and (n > 46):  # noqa PLR2004
        return True
    ans = False
    for a in abundant_array:
        if a > n:
            break
        if n - a in abundant_array:
            ans = True
            break
    return ans


@print_run_time
def sum_of_n_which_are_not_sum_of_two_abundants() -> int:
    # Given: by mathematical analysis, it can be shown that all integers greater than 28123
    # can be written as the sum of two abundant numbers.

    abundant_search_limit = 28124
    primes_array = primes_array_below(
        largest_prime_factor_upper_bound(abundant_search_limit) + 2 * math.log(abundant_search_limit),
    )

    # first of all make a list of abundant numbers
    abundant_array = get_abundant_array(abundant_search_limit, primes_array)

    ans = 0
    ans_list = []
    for n in range(1, abundant_search_limit):
        if not is_sum_of_two_abundant_numbers(n, abundant_array):
            ans_list.append(n)
            ans += n
    return ans


if __name__ == "__main__":
    print("Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.")
    print(sum_of_n_which_are_not_sum_of_two_abundants())
