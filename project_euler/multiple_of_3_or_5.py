from project_euler.decorators import print_run_time


def sum_to_n(n: int) -> int:
    if n < 0:
        msg = "n must be > 0"
        raise ValueError(msg)
    return n * (n + 1) // 2


def sum_xs_below_n(n: int, x: int) -> int:
    n_for_sum_to_n = (n - 1) // x
    return x * sum_to_n(n_for_sum_to_n)


@print_run_time
def sum_of_two_multiples_below_n(n: int, m1: int, m2: int) -> int:
    return sum_xs_below_n(n, m1) + sum_xs_below_n(n, m2) - sum_xs_below_n(n, m1 * m2)


if __name__ == "__main__":
    n = 1000
    m1 = 3
    m2 = 5
    print(f"Find the sum of all the multiples of 3 or 5 below {n}")
    print(f"answer = {sum_of_two_multiples_below_n(n, m1, m2)}")
