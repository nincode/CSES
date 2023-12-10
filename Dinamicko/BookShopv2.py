import time

MODULO = 10**9 + 7

l1 = input().split()
number_books = int(l1[0])
budget = int(l1[1])

l2 = input().split()
l3 = input().split()

prices = [0]
pages = [0]
for i in range(number_books):
    prices.append(int(l2[i]))
    pages.append(int(l3[i]))


dp = []
"""
for i in range(number_books + 1):
    dp.append([])
    for j in range(budget + 1):
        dp[i].append(-1)
"""

dp = [[-1 for i in range(budget + 1)] for j in range(number_books + 1)]
import sys

if number_books > 999:
    sys.setrecursionlimit(number_books * 2)


def countDP(dp):
    res = 0
    for d in dp:
        res += d.count(-1)
    return res


def recursive_solution(index, capacity):
    if dp[index][capacity] != -1:
        return dp[index][capacity]

    if index == 0 or capacity == 0:
        result = 0

    elif prices[index] > capacity:
        result = recursive_solution(index - 1, capacity)
    else:
        res1 = recursive_solution(index - 1, capacity)  # Don't buy
        res2 = recursive_solution(index - 1, capacity - prices[index]) + pages[index]
        result = max(res1, res2)

    dp[index][capacity] = result
    return result


t1 = time.time()
print(recursive_solution(number_books, budget) % MODULO)
t2 = time.time()
print(t2 - t1)
