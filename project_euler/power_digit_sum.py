from project_euler.decorators import print_run_time


@print_run_time
def sum_digits_of_2e(exponent: int) -> int:
    return sum(int(x) for x in str(2**exponent))


if __name__ == "__main__":
    exponent = 1000
    print(f"What is the sum of the digits of the number 2^{exponent}?")
    print(sum_digits_of_2e(exponent))
