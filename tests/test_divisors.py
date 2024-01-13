import pytest

from project_euler.divisors import calc_num_divisors, list_proper_divisors_using_list_of_primes
from project_euler.list_primes import list_primes_below

# TODO make list_proper_divisors_using_list_of_primes less complex
# TODO test for cases when list of primes is too short or empty
# TODO test for cases when input is a large prime

@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        (1, [1]),
        (2, [1]),
        (3, [1]),
        (4, [1, 2]),
        (5, [1]),
        (6, [1, 2, 3]),
        (7, [1]),
        (8, [1, 2, 4]),
        (9, [1, 3]),
        (28, [1, 2, 4, 7, 14]),
        (220, [1, 2, 4, 5, 10, 11, 20, 22, 44, 55, 110]),
        (284, [1, 2, 4, 71, 142]),
    ],
)
def test_list_proper_divisors_using_list_of_primes(test_input: int, expected: int) -> None:
    assert list_proper_divisors_using_list_of_primes(test_input) == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 3),
        (5, 2),
        (6, 4),
        (7, 2),
        (8, 4),
        (9, 3),
        (28, 6),
        (220, 12),
        (284, 6),
    ],
)
def test_calc_num_divisors_no_list_of_primes(test_input: int, expected: int) -> None:
    assert calc_num_divisors(test_input, [2]) == expected


@pytest.mark.parametrize(
    ("test_input", "expected"),
    [
        (1, 1),
        (2, 2),
        (3, 2),
        (4, 3),
        (5, 2),
        (6, 4),
        (7, 2),
        (8, 4),
        (9, 3),
        (28, 6),
        (220, 12),
        (284, 6),
    ],
)
def test_calc_num_divisors_long_list_of_primes(test_input: int, expected: int) -> None:
    list_of_primes = list_primes_below(1000)
    assert calc_num_divisors(test_input, list_of_primes) == expected
