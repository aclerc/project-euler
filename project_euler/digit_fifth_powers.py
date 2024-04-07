import math

from project_euler.decorators import print_run_time


@print_run_time
def sum_numbers_that_are_nth_powers_of_their_digits(n: int) -> int:
    n_digits = 1
    while math.log((9**n * n_digits), 10) > n_digits:
        n_digits += 1
    a = 9**n * n_digits
    ans = 0
    while a > 1:
        if sum(int(x) ** n for x in str(a)) == a:
            ans += a
        if sum(int(x) ** n for x in str(a)) < a:
            a = a - (a % 10)
        a -= 1
    return ans


if __name__ == "__main__":
    print("Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.")
    n = 5
    print(sum_numbers_that_are_nth_powers_of_their_digits(n))
