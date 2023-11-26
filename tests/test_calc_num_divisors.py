import pytest

from project_euler.list_primes import list_primes_below
from project_euler.num_divisors import calc_num_divisors


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
    ],
)
def test_calc_num_divisors_short_list_of_primes(test_input: int, expected: int) -> None:
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
    ],
)
def test_calc_num_divisors_long_list_of_primes(test_input: int, expected: int) -> None:
    list_of_primes = list_primes_below(100)
    assert calc_num_divisors(test_input, list_of_primes) == expected
