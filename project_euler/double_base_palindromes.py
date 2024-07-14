from project_euler.decorators import print_run_time
from project_euler.largest_palindrome_product import is_palindrome


@print_run_time
def sum_palindromic_base_10_and_2_less_than(limit: int) -> int:
    ans = 1  # 1 is a palindrome in both bases
    decimal = 0
    left_side_of_palindrome = 1
    while decimal < limit:
        binary = str(f"{left_side_of_palindrome:b}") + str(f"{left_side_of_palindrome:b}")[::-1]
        decimal = int(binary, 2)
        if is_palindrome(decimal):
            ans += decimal
        left_side_of_palindrome += 1
    decimal = 0
    # start with 10 in binary and do not reuse last digit on left side
    left_side_of_palindrome = 2
    while decimal < limit:
        binary = f"{left_side_of_palindrome:b}"[:-1] + f"{left_side_of_palindrome:b}"[::-1]
        decimal = int(binary, 2)
        if is_palindrome(decimal):
            ans += decimal
        left_side_of_palindrome += 1
    return ans


if __name__ == "__main__":
    print(
        "The decimal number, 585 = 1001001001 (binary), is palindromic in both bases. "
        "Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2."
    )
    print(sum_palindromic_base_10_and_2_less_than(10**6))
