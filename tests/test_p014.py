from project_euler.longest_collatz_sequence import longest_collatz_chain


def test_p014() -> None:
    start_num_upper = 999999
    ans = 837799
    assert longest_collatz_chain(start_num_upper) == ans
