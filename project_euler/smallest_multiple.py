import math

from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import get_next_prime


@print_run_time
def first_evenly_divisible_by_all_up_to_n(n: int) -> int:
    log_n = math.log(n)
    i = 2
    answer = 1
    while i < n:
        j = int(log_n // math.log(i))
        answer *= i**j
        i = get_next_prime(i)
    return answer


if __name__ == "__main__":
    n = 20
    print(f"What is the smallest positive number that is evenly divisible by all of the numbers from 1 to {n}?")
    print(f"answer is {first_evenly_divisible_by_all_up_to_n(n)}")
