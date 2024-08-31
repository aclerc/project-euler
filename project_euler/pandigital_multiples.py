import math

from project_euler.decorators import print_run_time


def _has_repeated_digits(x: str) -> bool:
    return len(set(x)) < len(x)


def _valid_answer_so_far(x: str) -> bool:
    return not (_has_repeated_digits(x) or "0" in x)


def _is_pandigital(*, concatenated_product: str, d: int) -> bool:
    return "".join(sorted(concatenated_product)) == "".join([str(x + 1) for x in range(d)])


@print_run_time
def largest_pandigital_from_concatenated_product(d: int) -> int:
    # to make the initial guess start with d and add on digits
    x = d
    while len(str(x)) < math.floor(d / 2):
        x = int(str(x) + str(x % 10 - 1))
    while x > 0:
        multiplier = 1
        concatenated_product = str(multiplier * x)
        while len(concatenated_product) < d:
            multiplier += 1
            concatenated_product += str(multiplier * x)
            if not _valid_answer_so_far(concatenated_product):
                break
            if _is_pandigital(concatenated_product=concatenated_product, d=d) and len(concatenated_product) == d:
                return int(concatenated_product)
        x -= 1
        if not _valid_answer_so_far(str(x)):
            x -= 1
    msg = "no answer found"
    raise RuntimeError(msg)


if __name__ == "__main__":
    d = 9
    print(
        f"What is the largest 1 to {d} pandigital {d}-digit number that can be formed as the concatenated product of "
        f"an integer with (1,2,...,n) where n > 1?"
    )
    print(f"answer: {largest_pandigital_from_concatenated_product(d)}")
