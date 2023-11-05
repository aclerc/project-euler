from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import get_next_prime


@print_run_time
def sum_primes_below(limit: int) -> int:
    answer = 0
    if limit < 6:  # noqa PLR2004 sieve code needs limit >= 6
        p = 0
        while True:
            p = get_next_prime(p)
            if p < limit:
                answer += p
            else:
                break
    else:
        # make a list of all odd numbers from 1 to n-1
        odd_ns = list(range(1, limit, 2))
        # sieve out 1 because it is not prime
        x = 1
        odd_ns[(x - 1)] = 0
        # special code for 2
        x = 2
        answer += x
        # special code for 3
        x = 3
        answer += x
        odd_ns[(x // 2) :: (x)] = [0] * len(odd_ns[(x // 2) :: (x)])
        x -= 2
        while x**2 < limit:
            if (x - 1) % 6 == 0:
                x += 4
            else:
                x += 2
            if odd_ns[(x // 2)] > 0:
                answer += x
                odd_ns[(x // 2) :: (x)] = [0] * len(odd_ns[(x // 2) :: (x)])
        answer += sum(odd_ns)
    return answer


if __name__ == "__main__":
    limit = 2 * 10**6
    print(f"Find the sum of all the primes below {limit}.")
    print(f"answer: {sum_primes_below(limit)}")
