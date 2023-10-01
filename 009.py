import time

start = time.time()

print("There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.")

# primitive pythagorean triples are in the form c = m**2 + n**2, b = 2mn, a = m**2 - n**2
# where one of m or n is odd

target_sum = 1000
answer_found = False
# guess values of m and n where m>n and one of m, n are even
m = 2
n = 1
s_ = 0
while not answer_found and s_ < target_sum / 2:
    s_ = 2 * m ** 2 + 2 * m * n
    if target_sum % s_ == 0:
        p = target_sum // s_
        a = p * (m ** 2 - n ** 2)
        b = p * 2 * m * n
        c = p * (m ** 2 + n ** 2)
        answer = a * b * c
        print(f"answer: {answer}")
        answer_found = True
        break
    if m - n > 2:
        n += 2
        print(f"m={m} n={n}")
    else:
        m += 1
        n = m % 2 + 1
        print(f"m={m} n={n}")

if target_sum == 1000 and answer != 31875000:
    print("answer is wrong")
print(f"time taken = {time.time() - start:.4f}s")
