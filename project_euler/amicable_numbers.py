import math

from project_euler.decorators import print_run_time
from project_euler.divisors import list_proper_divisors_using_list_of_primes
from project_euler.list_primes import list_primes_below


def sum_proper_divisors(x: int, list_of_primes: list[int]) -> int:
    return sum(list_proper_divisors_using_list_of_primes(x, list_of_primes))


@print_run_time
def sum_amicable_numbers_under(limit: int) -> int:
    ans = 0
    primes_list = list_primes_below(2*limit)
    spd_dict = {}
    for x in range(1,limit):
        spd = sum_proper_divisors(x,primes_list)
        spd_dict[x]=spd
    # for each key in spd_dict, if the value is >1 and not equal to the key
    for k, v in spd_dict.items():
        if v > 1 and k!=v:
            try:
                k_ = spd_dict[v]
            except KeyError:
                k_ = sum_proper_divisors(v,primes_list)
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
