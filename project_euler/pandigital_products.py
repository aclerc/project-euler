import math

from project_euler.decorators import print_run_time


def count_digits(x: int) -> int:
    return 1 + math.floor(math.log(x, 10))


@print_run_time
def sum_pandigital_products(n: int) -> int:
    pandigital_products = []
    a = 2
    b = a + 1
    c = a * b
    while count_digits(a) <= n // 3:
        while count_digits(a) + count_digits(b) + count_digits(c) < n:
            b += 1
            c = a * b
        while count_digits(a) + count_digits(b) + count_digits(c) == n:
            if "".join(sorted(str(a) + str(b) + str(c))) == "".join([str(x + 1) for x in range(n)]):
                pandigital_products.append(c)
            b += 1
            c = a * b
        a += 1
        b = a + 1
        c = a * b
        if count_digits(a) + count_digits(b) + count_digits(c) > n:
            break
    return sum(set(pandigital_products))


if __name__ == "__main__":
    n = 9
    print(
        "Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through "
        f"{n} pandigital."
    )
    print(sum_pandigital_products(n))
