import numpy as np

from project_euler.decorators import print_run_time


def cancel_digit(a: int, digit: str) -> int:
    return int(digit) if len(set(str(a)) - set(digit)) == 0 else int("".join(set(str(a)) - set(digit)))


def digit_cancelling_fraction(a: int, b: int) -> bool:
    for x in set(str(a)) & set(str(b)):
        a_ = cancel_digit(a, x)
        b_ = cancel_digit(b, x)
        if a * b_ == a_ * b:
            return True
    return False


@print_run_time
def denominator_of_digit_cancelling_two_digit_fractions() -> int:
    product_of_digit_cancelling_fractions_num = 1
    product_of_digit_cancelling_fractions_den = 1
    a = 11
    b = a + 1
    while a < 99:  # noqa PLR2004
        while b <= 99:  # noqa PLR2004
            if digit_cancelling_fraction(a, b):
                product_of_digit_cancelling_fractions_num *= a
                product_of_digit_cancelling_fractions_den *= b
            b += 1
            if str(b)[-1] == "0":
                b += 1
        a += 1
        if str(a)[-1] == "0":
            a += 1
        b = a + 1
    return product_of_digit_cancelling_fractions_den // np.gcd(
        product_of_digit_cancelling_fractions_den, product_of_digit_cancelling_fractions_num
    )


if __name__ == "__main__":
    print(
        "If the product of the four non-trivial digit cancelling fractions (example: 49/98=4/8) is given in its "
        "lowest common terms, find the value of the denominator."
    )
    print(denominator_of_digit_cancelling_two_digit_fractions())
