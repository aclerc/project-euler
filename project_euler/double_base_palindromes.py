from project_euler.decorators import print_run_time
from project_euler.largest_palindrome_product import is_palindrome


@print_run_time
def sum_palindromic_base_10_and_2_less_than(n: int) -> int:
    ans = 0
    for i in range(1, n):
        if is_palindrome(i) and is_palindrome(f"{i:b}"):
            ans += i
    return ans


if __name__ == "__main__":
    print(
        "The decimal number, 585 = 1001001001 (binary), is palindromic in both bases. "
        "Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."
    )
    print(sum_palindromic_base_10_and_2_less_than(10**6))
