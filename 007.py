import time

start = time.time()


def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True  # 2 and 3 are prime
    elif (n % 2 == 0) or (n % 3 == 0):
        return False  # 4 and 6 are sorted
    else:
        prime = True
        f = 5  # next factor not tested yet
        while f**2 <= n:
            prime = (n % f != 0) and (n % (f + 2) != 0)
            if not prime:
                break
            f += 6
        return prime


def get_next_prime(n):
    if n < 2:
        return 2
    else:
        p = n + (n % 2 + 1)
        while not is_prime(p):
            p += 2
        return p


# n = 6
n = 10001
# n = 100008 # should be 1299827
# n = 1000000 # 15485863, is that right? Yes according to https://t5k.org/
print(f"What is the {n}st prime number?")
i = 1
p = 2
while i < n:
    i += 1
    p = get_next_prime(p)
    if i < 20 or (i % 1000 == 0):
        print(f"i = {i} p = {p}")
print(f"answer: {p}")
print(f"time taken = {time.time()-start:.4f}s")
