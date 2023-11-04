from project_euler.decorators import print_run_time


@print_run_time
def sum_even_fibonacci_ns(max_n: int) -> int:
    answer = 2
    fib_2 = 1
    fib_1 = 2
    while (fib_1 + fib_2) < max_n:
        fib_0 = fib_1 + fib_2
        if fib_0 % 2 == 0:
            answer += fib_0
        fib_1, fib_2 = fib_0, fib_1
    return answer


if __name__ == "__main__":
    print(
        "By considering the terms in the Fibonacci sequence whose values do not exceed four million,"
        " find the sum of the even-valued terms.",
    )
    print(f"answer = {sum_even_fibonacci_ns(4000000-1)}")
