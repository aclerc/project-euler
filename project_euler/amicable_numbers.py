import numpy as np
import numpy.typing as npt

from project_euler.decorators import print_run_time
from project_euler.divisors import proper_divisors_array
from project_euler.list_primes import primes_array_below


def sum_proper_divisors(x: int, primes_array: npt.NDArray[np.int_]) -> int:
    return int(np.sum(proper_divisors_array(x, primes_array)))


@print_run_time
def sum_amicable_numbers_under(limit: int) -> int:
    ans = 0
    primes_array = primes_array_below(2 * limit)
    spd_dict = {}
    for x in range(1, limit):
        spd = sum_proper_divisors(x, primes_array)
        spd_dict[x] = spd
    # for each key in spd_dict, if the value is >1 and not equal to the key
    for k, v in spd_dict.items():
        if v > 1 and k != v:
            try:
                k_ = spd_dict[v]
            except KeyError:
                k_ = sum_proper_divisors(v, primes_array)
            if k == k_:
                print(f"{k} and {v} are an amicable pair")
                ans += k
    return ans


if __name__ == "__main__":
    limit = 10000
    print(
        f"Evaluate the sum of all the amicable numbers under {limit})?",
    )
    print(f"answer: {sum_amicable_numbers_under(limit)}")
