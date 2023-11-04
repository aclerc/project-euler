from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import get_next_prime


@print_run_time
def nth_prime(n: int) -> int:
    i = 1
    p = 2
    while i < n:
        i += 1
        p = get_next_prime(p)
        if i % 1000 == 0:
            print(f"i = {i} p = {p}")
    return p


if __name__ == "__main__":
    n = 10001
    print(f"What is the {n}st prime number?")
    print(f"answer: {nth_prime(n)}")
