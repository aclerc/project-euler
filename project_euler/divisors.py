import math
from itertools import product

import numpy as np
import numpy.typing as npt

from project_euler.largest_prime_factor import get_next_prime
from project_euler.list_primes import primes_array_below


def proper_divisors_using_prime_factors_dict(prime_factors_dict: dict[int, int]) -> npt.NDArray[np.int_]:
    if len(prime_factors_dict) == 0:
        return np.array([1])
    prime_factors_combos = list(product(*(range(value + 1) for value in prime_factors_dict.values())))[:-1]
    proper_divisors = []
    for pfc in prime_factors_combos:
        proper_divisor = 1
        for p, a in zip(prime_factors_dict.keys(), pfc, strict=False):
            proper_divisor *= p**a
        proper_divisors.append(proper_divisor)
    return np.array(sorted(proper_divisors))


def extend_primes_array_if_needed(primes_array: npt.NDArray[np.int_], limit: float) -> npt.NDArray[np.int_]:
    while max(primes_array) < limit:
        print("WARNING: list_of_primes is too short, extending list")
        primes_array = np.append(primes_array, get_next_prime(max(primes_array)))
    return primes_array


def largest_prime_factor_upper_bound(x: int) -> float:
    return x // 2 + 1 + 2 * math.log(x)


def make_or_extend_primes_of_needed(x: int, primes_array: npt.NDArray[np.int_] | None = None) -> npt.NDArray[np.int_]:
    limit = largest_prime_factor_upper_bound(x)
    if primes_array is None:
        primes_array = primes_array_below(limit)
    else:
        primes_array = extend_primes_array_if_needed(primes_array, limit)
    return primes_array


def proper_divisors_array(x: int, primes_array: np.ndarray | None = None) -> npt.NDArray[np.int_]:
    if x <= 3:  # noqa PLR2004
        return np.array([1])
    prime_array = np.array(make_or_extend_primes_of_needed(x, primes_array))
    len_prime_array = len(prime_array)
    if x in prime_array:
        return np.array([1])
    i = 0
    p = prime_array[i]
    prime_factors_dict = {}
    while x >= p and i < len_prime_array:
        p_div_count = 0
        while x % p == 0:
            x = x // p
            p_div_count += 1
        if p_div_count > 0:
            prime_factors_dict[p] = p_div_count
        if x == 1:
            break
        i += 1
        if i == len_prime_array:
            break
        p = prime_array[i]
    if len(prime_factors_dict) == 0:
        return np.array([1])
    return proper_divisors_using_prime_factors_dict(prime_factors_dict)


def calc_num_divisors(x: int, primes_array: np.ndarray | None = None) -> int:
    if x < 1:
        msg = "x must be >= 1"
        raise ValueError(msg)
    if x == 1:
        return 1
    return len(proper_divisors_array(x, primes_array)) + 1


def calc_num_divisors_using_list_of_primes(x: int, primes_array: np.ndarray) -> int:
    if not (isinstance(x, int) and x >= 1):
        msg = "x must be type int and > 0"
        raise ValueError(msg)
    primes_array = extend_primes_array_if_needed(primes_array, x // 2)
    return calc_num_divisors(x, primes_array)


if __name__ == "__main__":
    x = 11
    print(proper_divisors_array(x))
