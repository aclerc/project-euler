import math
from itertools import combinations_with_replacement

from project_euler.decorators import print_run_time


@print_run_time
def sum_of_numbers_equal_to_sum_of_factorial_of_their_digits() -> int:
    ans = 0
    for n_digits in range(2, 8):  # 7 is the max possible number of digits
        for digits in combinations_with_replacement("0123456789", n_digits):
            sum_fact = sum(math.factorial(int(x)) for x in digits)
            if sorted(x for x in str(sum_fact)) == sorted(digits) and len(str(sum_fact)) == n_digits:
                ans += sum_fact
    return ans


if __name__ == "__main__":
    print(
        "145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145. "
        "Find the sum of all numbers which are equal to the sum of the factorial of their digits. "
        "Note 1!=1 and 2!=2 are not sums so are not included."
    )
    print(sum_of_numbers_equal_to_sum_of_factorial_of_their_digits())
