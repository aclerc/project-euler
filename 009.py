import time
start = time.time()

print("There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.")

# TODO this can be done better by using the form c = m**2 + n**2, b = 2mn, a = m**2 - n**2 where one of m or n is odd to get a primitive pythagorean triple

answer_found = False

#guess a value of c
c = 500
d = 0
s = 1
while not answer_found:
    c += (s*d)
    d += 1
    s *= -1
    a = 1
    b = 1000 - c - a
    while (a <= b) and not answer_found:
        if c ** 2 == a ** 2 + b ** 2:
            answer_found = True
        else:
            a += 1
            b -= 1

print(f"a={a}")
print(f"b={b}")
print(f"c={c}")
print(f"answer: {a*b*c}")
print(f"time taken = {time.time()-start:.4f}s")