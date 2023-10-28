import time

start = time.time()

print("Longest Collatz Sequence")
print("The following iterative sequence is defined for the set of positive integers:")
print("n->n/2 (n is even)")
print("n->3n+1 (n is odd)")
print("Using the rule above and starting with 13, we generate the following sequence:")
print("13 40 20 10 5 16 8 4 2 1")
print("It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.")
print("Which starting number, under one million, produces the longest chain?")


def collatz_sequence(n):
    if n <= 0:
        return []
    if n <= 1:
        return [1]
    ns = []
    ns.append(n)
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        ns.append(n)
    return ns


def collatz_sequence_len(n, known_lens):
    if known_lens.get(n, None) is not None:
        return known_lens[n]
    elif n <= 0:
        return 0
    elif n <= 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_sequence_len(n // 2, known_lens)
    else:
        return 2 + collatz_sequence_len((3 * n + 1) // 2, known_lens)


start_num_upper = 1000000 - 1
n = 1
ns_tried_already = []
known_lens = {}
longest_seq = 0
best_n = n
while n <= start_num_upper:
    seq_len = collatz_sequence_len(n, known_lens)
    known_lens[n] = seq_len
    if seq_len > longest_seq:
        longest_seq = seq_len
        best_n = n
    n += 1
answer = best_n

# verify
collatz_sequence(best_n)
print(f"\nanswer={answer}")
if start_num_upper == 999999:
    assert answer == 837799
print(f"time taken = {time.time() - start:.4f}s")
