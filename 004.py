import time

start = time.time()


def is_palindrome(n):
    return str(n) == str(n)[::-1]


print("Find the largest palindrome made from the product of two 3-digit numbers.")
answer_found = False
answer = 0
for x in range(999, 99, -1):
    if x >= int(answer // 990):
        for y in range(990, 99, -1):
            if x % 11 == 0 or y % 11 == 0:  # based on analysis answer must be divisible by 11
                xty = x * y
                if is_palindrome(xty) and xty > answer:
                    answer = xty
                    print(f"{x} * {y} = {answer}")

print(f"answer = {answer}")
print(f"time taken = {time.time()-start:.4f}s")
