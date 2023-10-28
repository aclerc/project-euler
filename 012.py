import math
import time

start = time.time()

over_n_divisors = 5  # answer is 28
over_n_divisors = 500
print(f"What is the value of the first triangle number to have over {over_n_divisors} divisors?")


def num_divisors(x):
    if x < 1:
        return 0
    elif x == 1:
        return 1
    else:
        n = 2  # 1 and itself
        i = 2
        j = x
        while i <= j:
            if x % i == 0:
                j = x // i
                if i == j:
                    n += 1
                if i < j:
                    n += 2
            i += 1
        return n


# triangle numbers have the form n*(n+1)/2
# the first fatorial with over 500 divisors is math.factorial(11)
# so n is at least math.sqrt(4*2*math.factorial(10))
n = int(math.sqrt(4 * 2 * math.factorial(10)))
t = n * (n + 1) // 2
while num_divisors(t) <= over_n_divisors:
    n += 1
    t = n * (n + 1) // 2

# TODO could potentially speed this up by fidning the divisors of the two parts, n and n+1 with one being /2

answer = t
print(f"answer={t}")
if over_n_divisors == 500:
    assert answer == 76576500
print(f"time taken = {time.time() - start:.4f}s")
