from project_euler.decorators import print_run_time


def is_palindrome(n: int | str) -> bool:
    if isinstance(n, int):
        n = str(n)
    return int(n) == int(n[::-1])  # convert to int to ensure no leading 0


@print_run_time
def largest_palindrome_product_of_two_3_digit_numbers() -> int:
    answer = 0
    for x in range(999, 99, -1):
        if x >= int(answer // 990):
            for y in range(990, 99, -1):
                if x % 11 == 0 or y % 11 == 0:  # based on analysis answer must be divisible by 11
                    xty = x * y
                    if is_palindrome(xty) and xty > answer:
                        answer = xty
    return answer


if __name__ == "__main__":
    print("Find the largest palindrome made from the product of two 3-digit numbers.")
    print(f"answer = {largest_palindrome_product_of_two_3_digit_numbers()}")
