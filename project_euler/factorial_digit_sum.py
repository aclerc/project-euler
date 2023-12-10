import math


def sum_digits_factorial(x: int) -> int:
    fx = math.factorial(x)
    return sum(int(x) for x in str(fx))


if __name__ == "__main__":
    x = 100
    print(
        f"Find the sum of the digits in the number {x}!",
    )
    print(f"answer: {sum_digits_factorial(x)}")
