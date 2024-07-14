from project_euler.decorators import print_run_time
from project_euler.list_primes import list_primes_below


def _is_truncatable(p: int, *, primes_set: set[int], from_right: bool = True) -> bool:
    while len(str(p)) >= 2:  # noqa PLR2004
        if p not in primes_set:
            return False
        p = int(str(p)[1:]) if from_right else int(str(p)[:-1])
    return p in primes_set


@print_run_time
def sum_of_all_truncatable_primes() -> int:
    count_truncatable_primes = 0
    limit = 10**4
    # problem statement says there are only 11 primes truncatable from both left and right
    expected_count = 11
    while count_truncatable_primes < expected_count:
        ans = 0
        count_truncatable_primes = 0
        primes_set = set(list_primes_below(limit))
        for p in primes_set:
            if p <= 7:  # noqa PLR2004 problem statement says 1 digit primes do not count
                continue
            if _is_truncatable(p, primes_set=primes_set, from_right=True) and _is_truncatable(
                p, primes_set=primes_set, from_right=False
            ):
                print(f"{p=}")
                ans += p
                count_truncatable_primes += 1
                if count_truncatable_primes == expected_count:
                    return ans
        limit *= 10
    msg = "no answer found"
    raise RuntimeError(msg)


if __name__ == "__main__":
    print(
        "The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove "
        "digits from left to right, and remain prime at each stage: 3797, 797, 97 and 7. Similarly we can work "
        "from right to left: 3797, 379, 37, and 3."
        "Find the sum of the only eleven primes that are both truncatable from left to right and right to left."
    )
    print(f"answer: {sum_of_all_truncatable_primes()}")
