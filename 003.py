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


# n = 13195
n = 600851475143
# n = 13195 * 15487457
print(f"What is the largest prime factor of the number {n}?")
this_prime = 2
while not is_prime(n):
    if n % this_prime == 0:
        print(f"{this_prime} divides {n}")
        n = n // this_prime
    else:
        this_prime = get_next_prime(this_prime)
    if this_prime > (n**0.5):
        break
print(f"answer is {n}")
print(f"time taken = {time.time()-start:.4f}s")
