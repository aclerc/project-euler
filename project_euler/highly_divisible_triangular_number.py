import math

from project_euler.decorators import print_run_time


def num_divisors(x: int) -> int:
    if x < 1:
        num_div = 0
    elif x == 1:
        num_div = 1
    else:
        num_div = 2  # 1 and itself
        i = 2
        j = x
        while i <= j:
            if x % i == 0:
                j = x // i
                if i == j:
                    num_div += 1
                if i < j:
                    num_div += 2
            i += 1
    return num_div


def calc_a_b_and_t(n: int) -> tuple[int, int, int]:
    if n % 2 == 0:
        a = n + 1
        b = n // 2
    else:
        a = n
        b = (n + 1) // 2
    t = a * b
    return a, b, t


@print_run_time
def first_triangle_number_with_min_divisors(min_num_divisors: int) -> int:
    # from studying the first few triangular numbers it looks like
    # t's numdiv = a's numdiv * b's numdiv where a = n if n odd otherwise n+1
    # probably because a and b never have a common divisor
    # so for t to have min_num_divisors, a or b must have at least sqrt(min_num_divisors)
    n = 1
    while num_divisors(math.factorial(n)) <= math.sqrt(min_num_divisors):
        n += 1
    a, b, t = calc_a_b_and_t(n)
    while (num_divisors(a) * num_divisors(b)) < min_num_divisors:
        n += 1
        a, b, t = calc_a_b_and_t(n)
    return t


if __name__ == "__main__":
    min_num_divisors = 500 + 1
    print(f"What is the value of the first triangle number to have over {min_num_divisors-1} divisors?")
    print(f"answer = {first_triangle_number_with_min_divisors(min_num_divisors)}")
