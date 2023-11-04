from project_euler.decorators import print_run_time


@print_run_time
def sum_of_squares_minus_square_of_sum(n: int) -> int:
    square_sum = (n * (n + 1) // 2) ** 2
    sum_squares = (2 * n**3 + 3 * n**2 + n) // 6  # figured out from lego
    return square_sum - sum_squares

if __name__ == "__main__":
    n = 100
    print(f"Find the difference between the sum of the squares of the first {n} natural numbers and the square of the sum.")
    print(f"answer is {sum_of_squares_minus_square_of_sum(n)}")
