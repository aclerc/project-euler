from project_euler.lexicographic_permutations import nth_lexicographic_permutation


def test_p024() -> None:
    largest_digit = 9
    n = 1000000
    ans = "2783915460"
    assert nth_lexicographic_permutation(n, largest_digit) == ans
