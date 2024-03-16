import itertools

from project_euler.decorators import print_run_time


@print_run_time
def nth_lexicographic_permutation(n: int, largest_digit: int) -> str:
    perms = itertools.permutations(range(largest_digit + 1))
    for index, value in enumerate(perms):
        if index == n - 1:
            nth_element = value
            break
    return "".join([str(x) for x in nth_element])


if __name__ == "__main__":
    print(
        "A permutation is an ordered arrangement of objects. "
        "For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. "
        "If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. "
        "What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?"
    )
    largest_digit = 9
    n = 1000000
    print(f"answer = {nth_lexicographic_permutation(n,largest_digit)}")
