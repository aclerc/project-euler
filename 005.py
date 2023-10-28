import math
import time

start = time.time()


def is_prime(n):
    if n < 2:
        return False
    else:
        prime = True
        f = 2
        while f <= n // f:
            prime = n % f != 0
            if not prime:
                break
            f += 1
        return prime


def get_next_prime(n):
    if n < 2:
        return 2
    else:
        p = n + (n % 2 + 1)
        while not is_prime(p):
            p += 2
        return p


n = 20
print(f"What is the smallest positive number that is evenly divisible by all of the numbers from 1 to {n}?")
log_n = math.log(n)
i = 2
answer = 1
while i < n:
    j = int(log_n // math.log(i))
    answer *= i**j
    i = get_next_prime(i)
print(f"answer is {answer}")
print(f"time taken = {time.time()-start:.4f}s")
