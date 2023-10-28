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
            if (p - 1) % 6 == 0:
                p += 4
            else:
                p += 2
        return p


n = 2000000
print(f"Find the sum of all the primes below {n}")
if n < 6:
    p = 0
    answer = 0
    while True:
        p = get_next_prime(p)
        if p < n:
            answer += p
        else:
            break
else:
    # make a list of all odd numbers from 1 to n-1
    odd_ns = [x for x in range(1, n, 2)]
    # sieve out 1 because it is not prime
    answer = 0
    x = 1
    odd_ns[(x - 1)] = 0
    # special code for 2
    x = 2
    answer += x
    # special code for 3
    x = 3
    answer += x
    odd_ns[(x // 2) :: (x)] = [0] * len(odd_ns[(x // 2) :: (x)])
    x -= 2
    while x**2 < n:
        if (x - 1) % 6 == 0:
            x += 4
        else:
            x += 2
        if odd_ns[(x // 2)] > 0:
            answer += x
            odd_ns[(x // 2) :: (x)] = [0] * len(odd_ns[(x // 2) :: (x)])
    answer += sum(odd_ns)

print(f"answer={answer}")
if n == 2000000 and answer != 142913828922:
    print("answer is wrong")
print(f"time taken = {time.time() - start:.4f}s")
