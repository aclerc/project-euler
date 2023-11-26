from project_euler.decorators import print_run_time

collatz_sequence_len_cache: dict[int, int] = {}


def calc_collatz_sequence_len(n: int) -> int:
    if n <= 1:
        seq_len = 1
    elif n % 2 == 0:
        seq_len = 1 + calc_collatz_sequence_len(n // 2)
    else:
        seq_len = 2 + calc_collatz_sequence_len((3 * n + 1) // 2)
    return seq_len


def get_collatz_sequence_len(n: int) -> int:
    if n in collatz_sequence_len_cache:
        seq_len = collatz_sequence_len_cache[n]
    else:
        seq_len = calc_collatz_sequence_len(n)
        collatz_sequence_len_cache[n] = seq_len
    return seq_len


@print_run_time
def longest_collatz_chain(start_num_upper: int) -> int:
    n = start_num_upper
    longest_seq = 0
    best_n = n
    # the longest sequence must visit the top half of the problem space
    while n > start_num_upper / 2:
        seq_len = get_collatz_sequence_len(n)
        if seq_len > longest_seq:
            longest_seq = seq_len
            best_n = n
            print(f"n={best_n}")
            print(f"longest_seq={longest_seq}")
        n -= 1
    return best_n


if __name__ == "__main__":
    print("Longest Collatz Sequence")
    print("The following iterative sequence is defined for the set of positive integers:")
    print("n->n/2 (n is even)")
    print("n->3n+1 (n is odd)")
    print("Using the rule above and starting with 13, we generate the following sequence:")
    print("13 40 20 10 5 16 8 4 2 1")
    print("It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.")
    start_num_upper = 999999
    print(f"Which starting number, under {start_num_upper+1}, produces the longest chain?")
    print(f"\nanswer={longest_collatz_chain(start_num_upper)}")
