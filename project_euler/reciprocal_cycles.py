import numpy as np

from project_euler.decorators import print_run_time
from project_euler.list_primes import primes_array_below


@print_run_time
def d_with_longest_recurring_decimal_cycle(d_limit: int) -> int:
    prime_array = primes_array_below(d_limit + 1)
    if len(prime_array) > 0:
        prime_array = np.delete(prime_array, 0)
    if len(prime_array) > 1:
        prime_array = np.delete(prime_array, 1)

    recurring_cycle_lens = np.zeros(len(prime_array), dtype=int)
    for i, p in enumerate(prime_array):
        recurring_cycle_lens[i] = 1
        num_to_divide = recurring_cycle_lens[i] * 9
        while num_to_divide % p != 0:
            recurring_cycle_lens[i] += 1
            num_to_divide = int(str(num_to_divide) + "9")
    return prime_array[np.argmax(recurring_cycle_lens)]


if __name__ == "__main__":
    d_limit = 1000
    print(
        f"Find the value of d < {d_limit+1} for which "
        "1/d contains the longest recurring cycle in its decimal fraction part."
    )
    print(f"answer = {d_with_longest_recurring_decimal_cycle(d_limit)}")
