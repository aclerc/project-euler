import time

start = time.time()


def sum_to_n(n):
    return n * (n + 1) // 2


def sum_xs_below_n(n, x):
    n_for_sum_to_n = (n - 1) // x
    return x * sum_to_n(n_for_sum_to_n)


n = 1000
print(f"Find the sum of all the multiples of 3 or 5 below {n}")
print(f"answer = {sum_xs_below_n(n, 3) + sum_xs_below_n(n, 5) - sum_xs_below_n(n, 15)}")
print(f"time taken = {time.time()-start:.4f}s")
