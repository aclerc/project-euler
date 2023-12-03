from num2words import num2words

from project_euler.decorators import print_run_time


@print_run_time
def count_letters_to(n: int) -> int:
    return sum(len(num2words(x).replace(" ", "").replace("-", "")) for x in range(1, n + 1))


if __name__ == "__main__":
    n = 1000
    print(f"If all the numbers from 1 to {n} inclusive were written out in words, how many letters would be used?")
    print(count_letters_to(n))
