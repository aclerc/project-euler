from project_euler.decorators import print_run_time


@print_run_time
def index_first_fibonacci_with_n_digits(n: int) -> int:
    f1 = 1
    f2 = 1
    f3 = f1 + f2
    f_idx = 3
    while f3 < 10 ** (n - 1):
        f1, f2 = f2, f3
        f3 = f1 + f2
        f_idx += 1
    return f_idx


if __name__ == "__main__":
    n = 1000
    print(
        "The 12th term, 144, is the first term to contain three digits. "
        f"What is the index of the first term in the Fibonacci sequence to contain {n} digits?"
    )
    print(f"answer = {index_first_fibonacci_with_n_digits(n)}")
