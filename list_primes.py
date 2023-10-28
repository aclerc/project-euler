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


n = 1000
p = 2
i = 1
while i <= n:
    print(f"i={i} p={p}")
    p = get_next_prime(p)
    i += 1

print(f"time taken = {time.time()-start:.4f}s")
