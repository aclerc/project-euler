import numpy as np

from project_euler.decorators import print_run_time


def count_ways_with_next_coin(pence_to_make: int, last_coin_value: int | None) -> int:
    smallest_coin_value = 2
    if last_coin_value == smallest_coin_value:
        return 1
    this_coin_value = 200 if not last_coin_value else last_coin_value // 2
    invalid_coin_value = 25
    if this_coin_value == invalid_coin_value:
        this_coin_value = 20
    ans = 0
    for x in range(pence_to_make // this_coin_value + 1):
        if x * this_coin_value > pence_to_make:
            break
        ans += count_ways_with_next_coin(pence_to_make - this_coin_value * x, this_coin_value)
    return ans


@print_run_time
def count_ways_to_make_pence_recursive(pence_to_make: int) -> int:
    return count_ways_with_next_coin(pence_to_make, None)


@print_run_time
def count_ways_to_make_pence(pence_to_make: int) -> int:
    coins = 1, 2, 5, 10, 20, 50, 100, 200
    ways = np.zeros(pence_to_make + 1)
    ways[0] = 1
    for i in range(len(coins)):
        for j in range(coins[i], pence_to_make + 1):
            ways[j] += ways[j - coins[i]]
    return int(ways[pence_to_make])


if __name__ == "__main__":
    pounds_to_make = 100
    print(f"How many different ways can £{pounds_to_make} be made using any number of coins?")
    pence_to_make = pounds_to_make * 100
    print(count_ways_to_make_pence(pence_to_make))
