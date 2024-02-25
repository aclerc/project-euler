import numpy as np
import pytest

from project_euler.divisors import calc_num_divisors, calc_num_divisors_using_list_of_primes, proper_divisors_array
from project_euler.list_primes import primes_array_below


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
        (2018, [1, 2, 1009]),
    ],
)
def test_list_proper_divisors_no_list_of_primes(test_input: int, expected: list[int]) -> None:
    # test without providing primes list
    expected_arr = np.array(expected)
    assert np.array_equal(proper_divisors_array(test_input), expected_arr)
    assert calc_num_divisors(test_input) == (1 if test_input == 1 else len(expected_arr) + 1)
    # test with providing too short primes list
    primes_array = np.array([2])
    assert np.array_equal(proper_divisors_array(test_input, primes_array), expected_arr)
    assert calc_num_divisors(test_input, primes_array) == (1 if test_input == 1 else len(expected_arr) + 1)
    # test with providing plenty of primes
    primes_array = primes_array_below(2018)
    assert np.array_equal(proper_divisors_array(test_input, primes_array), expected_arr)
    assert calc_num_divisors(test_input, primes_array) == (1 if test_input == 1 else len(expected_arr) + 1)


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
    assert calc_num_divisors_using_list_of_primes(test_input, np.array([2])) == expected


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
    primes_array = primes_array_below(1000)
    assert calc_num_divisors_using_list_of_primes(test_input, primes_array) == expected
