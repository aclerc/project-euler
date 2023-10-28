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
    if n <= 1:
        return [1]
    ns = []
    ns.append(n)
    while n!=1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n+1
        ns.append(n)
    return ns

def collatz_sequence_len(n, known_lens):
    if n <= 1:
        return 1

    if known_lens.get(n, None) is not None:
        return known_lens[n]

    ns = []
    ns.append(n)
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n+1
        if known_lens.get(n, None) is not None:
            return known_lens[n] + len(ns)
        else:
            ns.append(n)
    return len(ns)

start_num_upper = 1000000 - 1
n = 1
ns_tried_already = []
known_lens = {}
longest_seq = 0
best_n = n
loop_count = 0
while n <= start_num_upper:
    loop_count += 1
    seq_len = collatz_sequence_len(n, known_lens)
    known_lens[n] = seq_len
    if seq_len > longest_seq:
        longest_seq = seq_len
        best_n = n
        print(f"n={best_n}")
        print(f"longest_seq={longest_seq}")
    n += 1
answer=best_n

# verify
collatz_sequence(best_n)
print(f"\nanswer={answer}")
if start_num_upper == 999999 and answer != 837799:
    print("answer is wrong")
print(f"time taken = {time.time() - start:.4f}s")