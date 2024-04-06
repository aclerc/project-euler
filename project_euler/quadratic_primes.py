import math

from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import is_prime
from project_euler.list_primes import list_primes_below


@print_run_time
def product_coeffs_for_max_quadratic_primes(limit: int) -> int:
    primes = list_primes_below(limit + 1)
    best_a = 1
    best_b = 41
    n = 39  # given in problem statement for a=1, b=41
    n += 1
    for b in reversed(primes):
        smallest_a = math.ceil((-b - n**2) / n)
        if smallest_a % 2 == 0:
            smallest_a += 1
        for a in range(smallest_a, limit, 2):
            if is_prime(n**2 + a * n + b):
                # check if it is prime all the way down to n=0
                for n_ in range(n - 1, 0, -1):
                    if not is_prime(n_**2 + a * n_ + b):
                        break
                    if n_ == 1:
                        # see how high up it goes
                        while is_prime(n**2 + a * n + b):
                            n += 1
                        n -= 1
                        best_a = a
                        best_b = b
    return best_a * best_b


if __name__ == "__main__":
    print(
        "Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum "
        "number of primes for consecutive values of n, starting with 0"
    )
    limit = 1000
    print(product_coeffs_for_max_quadratic_primes(limit))
