
from project_euler.decorators import print_run_time
from project_euler.list_primes import list_primes_below


@print_run_time
def sum_primes_below(limit: int) -> int:
    return sum(list_primes_below(limit))


if __name__ == "__main__":
    limit = 2 * 10**6
    print(f"Find the sum of all the primes below {limit}.")
    print(f"answer: {sum_primes_below(limit)}")
