import math

from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import get_next_prime


@print_run_time
def list_primes_below(limit: float) -> list[int]:
    limit = math.ceil(limit)
    list_of_primes = []
    if limit < 6:  # noqa PLR2004 sieve code needs limit >= 6
        p = get_next_prime(0)
        while p < limit:
            list_of_primes.append(p)
            p = get_next_prime(p)
    else:
        # make a list of all odd numbers from 1 to n-1
        odd_ns = list(range(1, limit, 2))
        xs_used = [2]
        # sieve out 1 because it is not prime
        odd_ns[0] = 0
        # special code for 3
        x = 3
        xs_used.append(x)
        odd_ns[(x // 2) :: x] = [0] * len(odd_ns[(x // 2) :: x])
        x -= 2
        while x**2 < limit:
            if (x - 1) % 6 == 0:
                x += 4
            else:
                x += 2
            if odd_ns[(x // 2)] > 0:
                xs_used.append(x)
                odd_ns[(x // 2) :: (x)] = [0] * len(odd_ns[(x // 2) :: (x)])
        list_of_primes = xs_used + [x for x in odd_ns if x > 0]
    return list_of_primes


if __name__ == "__main__":
    print(list_primes_below(100))
