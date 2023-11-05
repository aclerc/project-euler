from project_euler.largest_palindrome_product import largest_palindrome_product_of_two_3_digit_numbers


def test_p004() -> None:
    ans = 906609
    assert largest_palindrome_product_of_two_3_digit_numbers() == ans
