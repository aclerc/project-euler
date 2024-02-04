import pytest

from project_euler.divisors import calc_num_divisors, calc_num_divisors_using_list_of_primes, list_proper_divisors
from project_euler.list_primes import list_primes_below


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
        (1009, [1]),
    ],
)
def test_list_proper_divisors_no_list_of_primes(test_input: int, expected: list[int]) -> None:
    # test without providing primes list
    assert list_proper_divisors(test_input) == expected
    assert calc_num_divisors(test_input) == (1 if test_input == 1 else len(expected) + 1)
    # test with providing too short primes list
    list_of_primes = [2]
    assert list_proper_divisors(test_input, list_of_primes) == expected
    assert calc_num_divisors(test_input, list_of_primes) == (1 if test_input == 1 else len(expected) + 1)
    # test with providing plenty of primes
    list_of_primes = list_primes_below(2000)
    assert list_proper_divisors(test_input, list_of_primes) == expected
    assert calc_num_divisors(test_input, list_of_primes) == (1 if test_input == 1 else len(expected) + 1)


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
def test_calc_num_divisors_short_list_of_primes(test_input: int, expected: int) -> None:
    assert calc_num_divisors_using_list_of_primes(test_input, [2]) == expected


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
    assert calc_num_divisors_using_list_of_primes(test_input, list_of_primes) == expected
