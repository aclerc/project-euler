from project_euler.decorators import print_run_time


def is_prime(n: int) -> bool:
    smallest_prime = 2
    if n < smallest_prime:
        prime = False
    elif n <= 3:  # noqa PLR2004
        prime = True  # 2 and 3 are prime
    elif (n % 2 == 0) or (n % 3 == 0):
        prime = False
    else:
        prime = True
        f = 5  # next prime after 3
        while f**2 <= n:
            prime = (n % f != 0) and (n % (f + 2) != 0)
            if not prime:
                break
            f += 6
    return prime


def get_next_prime(n: int) -> int:
    smallest_prime = 2
    if n < smallest_prime:
        p = smallest_prime
    else:
        p = n + (n % 2 + 1)
        while not is_prime(p):
            if (p - 1) % 6 == 0:
                p += 4
            else:
                p += 2
    return p


@print_run_time
def largest_prime_factor(n: int) -> int:
    this_prime = 2
    while not is_prime(n):
        if n % this_prime == 0:
            print(f"{this_prime} divides {n}")
            n = n // this_prime
        else:
            this_prime = get_next_prime(this_prime)
        if this_prime > (n**0.5):
            break
    return n


if __name__ == "__main__":
    n = 600851475143
    print(f"What is the largest prime factor of the number {n}?")
    print(f"answer = {largest_prime_factor(n)}")
