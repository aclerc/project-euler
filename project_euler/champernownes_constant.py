import math

from project_euler.decorators import print_run_time


@print_run_time
def multiply_champernowne_digits(digits: list[int]) -> int:
    numbers_needed = math.ceil(2 * max(digits) / math.log(max(digits) + 1, 10))
    champernowne = "".join([str(x) for x in range(1, numbers_needed + 1)])
    ans = 1
    for digit in digits:
        ans *= int(champernowne[digit - 1])
    return ans


print(multiply_champernowne_digits([1, 10, 100, 1000, 10000, 100000, 1000000]))
