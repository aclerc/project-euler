import math

import numpy as np
import numpy.typing as npt

from project_euler.decorators import print_run_time
from project_euler.divisors import calc_num_divisors_using_list_of_primes
from project_euler.list_primes import primes_array_below


def calc_a_b_and_t(n: int) -> tuple[int, int, int]:
    if n % 2 == 0:
        a = n + 1
        b = n // 2
    else:
        a = n
        b = (n + 1) // 2
    t = a * b
    return a, b, t


num_divisors_cache: dict[int, int] = {}


def get_num_divisors(x: int, prime_array: npt.NDArray[np.int_]) -> int:
    if x in num_divisors_cache:
        nd = num_divisors_cache[x]
    else:
        nd = calc_num_divisors_using_list_of_primes(x, prime_array)
        num_divisors_cache[x] = nd
    return nd


@print_run_time
def first_triangle_number_with_min_divisors(min_num_divisors: int) -> int:
    # from studying the first few triangular numbers it looks like
    # t's numdiv = a's numdiv * b's numdiv where a = n if n odd otherwise n+1
    # probably because a and b never have a common divisor
    # so for t to have min_num_divisors, a or b must have at least sqrt(min_num_divisors)
    n = 1
    primes_array = primes_array_below(min_num_divisors * 20)
    while get_num_divisors(math.factorial(n), primes_array) <= math.sqrt(min_num_divisors):
        n += 1
    a, b, t = calc_a_b_and_t(n)
    while (get_num_divisors(a, primes_array) * get_num_divisors(b, primes_array)) < min_num_divisors:
        n += 1
        a, b, t = calc_a_b_and_t(n)
    return t


if __name__ == "__main__":
    min_num_divisors = 500 + 1
    print(f"What is the value of the first triangle number to have over {min_num_divisors-1} divisors?")
    print(f"answer = {first_triangle_number_with_min_divisors(min_num_divisors)}")
