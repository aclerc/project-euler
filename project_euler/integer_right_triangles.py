import math

from project_euler.decorators import print_run_time


def _integer_triangle_solutions(p: int) -> int:
    solutions = 0
    for a in range(1, math.floor(p / 3) + 1):
        b = math.ceil((p - a) / 2)
        c = math.sqrt(a**2 + b**2)
        while (a + b + c) > p:
            b -= 1
            c = math.sqrt(a**2 + b**2)
        for rc in (math.floor(c), math.ceil(c)):
            if a + b + rc == p and a**2 + b**2 == rc**2:
                solutions += 1
    return solutions


@print_run_time
def maximum_integer_traingles(p: int) -> int:
    most_solutions = 0
    p_with_most_solutions = p
    while p >= (3 + 4 + 5):  # PLR2004 3, 4, 5 is the smallest solution
        this_p_solutions = _integer_triangle_solutions(p)
        if this_p_solutions > most_solutions:
            most_solutions = this_p_solutions
            p_with_most_solutions = p
        p -= 1
    return p_with_most_solutions


if __name__ == "__main__":
    print(
        "If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly "
        "three solutions for p=120. For which value of p <= 1000, is the number of solutions maximised?"
    )
    print(f"answer: {maximum_integer_traingles(1000)}")
