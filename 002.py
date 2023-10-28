import time

start = time.time()

print(
    "By considering the terms in the Fibonacci sequence whose values do not exceed four million,"
    " find the sum of the even-valued terms."
)
answer = 2
fib_2 = 1
fib_1 = 2
while (fib_1 + fib_2) < 4000000:
    fib_0 = fib_1 + fib_2
    if fib_0 % 2 == 0:
        answer += fib_0
    fib_1, fib_2 = fib_0, fib_1
print(answer)
print(f"time taken = {time.time()-start:.4f}s")
