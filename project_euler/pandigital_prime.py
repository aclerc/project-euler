import itertools

from project_euler.decorators import print_run_time
from project_euler.largest_prime_factor import is_prime


@print_run_time
def largest_pandigital_prime() -> int:
    for num_digits in range(7, 3, -1):  # 9 and 8 digit pandigitals would always be divisible by 3
        digits = [str(x + 1) for x in range(num_digits)]
        possible_answers = [int("".join(x)) for x in itertools.permutations(digits)]
        for p in reversed(possible_answers):
            if is_prime(p):
                return p
    msg = "no answer found"
    raise RuntimeError(msg)


if __name__ == "__main__":
    print(
        "We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. "
        "For example, 2143 is a 4-digit pandigital and is also prime. What is the largest n-digit pandigital prime "
        "that exists?"
    )
    print(f"answer: {largest_pandigital_prime()}")
