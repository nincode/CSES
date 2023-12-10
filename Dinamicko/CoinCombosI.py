MODULO = 10**9 + 7

dp = []
coins = []

l1 = input().split()

n = int(l1[1])
x = int(l1[0])

l2 = input().split()

for i in range(n + 1):
    dp.append(0)
dp[0] = 1
for i in range(x):
    coins.append(int(l2[i]))

for i in range(n):
    if dp[i] != 0:
        for j in range(x):
            if i + coins[j] <= n:
                dp[i + coins[j]] = (dp[i] + dp[i + coins[j]]) % MODULO


print(dp[n])
