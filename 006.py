import time
import math
start = time.time()

n = 100
print(f"Find the difference between the sum of the squares of the first {n} natural numbers and the square of the sum.")
square_sum = (n * (n + 1) // 2) ** 2
sum_squares = (2*n**3 + 3*n**2 + n)//6 # figured out by supposing f(n) = a*n**3 + b*n**2 + c*n + d 
answer = square_sum - sum_squares
print(f"answer is {answer}")
print(f"time taken = {time.time()-start:.4f}s")
