# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# print(factorial(4))

import time
import numpy as np
x = np.random.random(100000000)

# Case 1
start = time.time()
sum(x) / len(x)
print(time.time() - start)

# Case 2
start = time.time()
np.mean(x)
print(time.time() - start)