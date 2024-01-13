import math
from itertools import product

from project_euler.largest_prime_factor import get_next_prime
from project_euler.list_primes import list_primes_below


def list_proper_divisors_using_list_of_primes(x: int, list_of_primes: list[int] | None = None) -> list[int]:
    if x <= 3:  # noqa PLR2004
        return [1]
    if list_of_primes is None:
        list_of_primes = list_primes_below(x // 2 + 1 + 2 * math.log(x))
    if max(list_of_primes) < x // 2:
        msg = "list of primes might be too short"
        raise ValueError(msg)
    i = 0
    p = list_of_primes[i]
    prime_factors_dict = {}
    while x >= p and i < len(list_of_primes):
        p_div_count = 0
        while x % p == 0:
            x = x // p
            p_div_count += 1
        if p_div_count > 0:
            prime_factors_dict[p] = p_div_count
        if x == 1:
            break
        i += 1
        if i == len(list_of_primes):
            break
        p = list_of_primes[i]
    if len(prime_factors_dict) == 0:
        return [1]
    prime_factors_combos = list(product(*(range(value + 1) for value in prime_factors_dict.values())))[:-1]
    proper_divisors = []
    for pfc in prime_factors_combos:
        proper_divisor = 1
        for p, a in zip(prime_factors_dict.keys(), pfc, strict=False):
            proper_divisor *= p**a
        proper_divisors.append(proper_divisor)
    return sorted(proper_divisors)


def calc_num_divisors_using_list_of_primes(x: int, list_of_primes: list[int] | None = None) -> int:
    if x < 1:
        msg = "x must be >= 1"
        raise ValueError(msg)
    if x == 1:
        return 1
    return len(list_proper_divisors_using_list_of_primes(x, list_of_primes)) + 1


def calc_num_divisors(x: int, list_of_primes: list[int]) -> int:
    if not (isinstance(x, int) and x >= 1):
        msg = "x must be type int and > 0"
        raise ValueError(msg)
    while max(list_of_primes) < x // 2:
        print("WARNING: list_of_primes is too short, extending list")
        list_of_primes.append(get_next_prime(max(list_of_primes)))
    return calc_num_divisors_using_list_of_primes(x, list_of_primes)


if __name__ == "__main__":
    x = 11
    print(list_proper_divisors_using_list_of_primes(x))
