import time
start = time.time()

# TODO the below code takes >3s. Use a sieve instead

def is_prime(n):
    if n < 2:
        return False
    elif n < 4:
        return True # 2 and 3 are prime
    elif (n % 2 == 0) or (n % 3 == 0):
        return False # 4 and 6 are sorted
    else:
        prime = True
        f = 5 # next factor not tested yet
        while f**2 <= n:
            prime = (n % f != 0) and (n % (f+2) != 0)
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
            #TODO can add by 4 every other time because primes above 3 take the form 6k +/- 1
            p += 2
        return p


n = 2000000
print(f"Find the sum of all the primes below {n}.")
p = 0
answer = 0
while True:
    p = get_next_prime(p)
    if p < n:
        answer += p
    else:
        break
print(f"answer: {answer}")
print(f"time taken = {time.time()-start:.4f}s")
