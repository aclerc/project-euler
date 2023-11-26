import math

from project_euler.largest_prime_factor import get_next_prime
from project_euler.list_primes import list_primes_below


def calc_num_divisors_with_list_of_primes(x: int, list_of_primes: list[int]) -> int:
    if max(list_of_primes) < x // 2:
        msg = "list of primes is too short"
        raise ValueError(msg)
    num_div = 1
    i = 0
    if x in list_of_primes:
        num_div = 2
    else:
        p = list_of_primes[i]
        while math.ceil(x / 2) >= p:
            a = 1
            while x % p == 0:
                x = x // p
                a += 1
            num_div *= a
            if x in list_of_primes:
                num_div *= 2
                break
            if i == (len(list_of_primes) - 1):
                if a == 1:
                    num_div *= 2
                break
            i += 1
            p = list_of_primes[i]
    return num_div


def calc_num_divisors(x: int, list_of_primes: list[int]) -> int:
    if not (isinstance(x, int) and x >= 1):
        msg = "x must be type int and > 0"
        raise ValueError(msg)
    while max(list_of_primes) < x // 2:
        print("WARNING: list_of_primes is too short, extending list")
        list_of_primes.append(get_next_prime(max(list_of_primes)))
    return calc_num_divisors_with_list_of_primes(x, list_of_primes)


if __name__ == "__main__":
    list_of_primes = list_primes_below(29)
    for x in range(1, 29):
        print(f"x={x}")
        print(calc_num_divisors(x, list_of_primes))
