import numpy as np
import numpy.typing as npt

from project_euler.decorators import print_run_time
from project_euler.list_primes import primes_array_below


def is_circular_prime(p: int, p_array: npt.NDArray[np.int_]) -> bool:
    if p == 2:  # noqa PLR2004
        return True
    if any(int(x) % 2 == 0 for x in str(p)):
        return False
    return all(int(str(p)[i:] + str(p)[: -len(str(p)) + i]) in p_array for i in range(len(str(p))))


@print_run_time
def count_circular_primes_below(n: int) -> int:
    ans = 0
    p_array = primes_array_below(n)
    for p in p_array:
        if is_circular_prime(p, p_array):
            ans += 1
    return ans


if __name__ == "__main__":
    print(
        "The number, 197, is called a circular prime because all rotations of the digits: "
        "197, 971, and 719, are themselves prime. "
        "How many circular primes are there below one million?"
    )
    print(count_circular_primes_below(10**6))
