import time
import numpy as np

import sys

sys.stdin = open("test_input.txt", "r")


l1 = input().split()
n_books = int(l1[0])
budget = int(l1[1])

line2 = input().split()  # Values
line3 = input().split()  # Weights

vals = np.array(line2, dtype=int)
weights = np.array(line3, dtype=int)
grid = np.zeros((n_books, budget + 1), dtype=int)

time_start = time.perf_counter()
for i in range(n_books):
    for w in range(budget + 1):
        if w < weights[i]:
            grid[i][w] = grid[i - 1][w]
        else:
            grid[i][w] = max(vals[i] + grid[i - 1][w - weights[i]], grid[i - 1][w])

## 0.288
time_elapsed = time.perf_counter() - time_start
print(f"Elapsed: {time_elapsed:0.3f}")


print(grid[-1][-1])
a = 2
