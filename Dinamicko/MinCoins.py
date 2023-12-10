maxX = 10**6
INF = -2
N, X = map(int, input().split())
coins = []
l2 = input().split()
dp = []
for i in range(N):
    coins.append(int(l2[i]))

for i in range(X+1):
    dp.append(INF)

for i in range(N):
    c = coins[i]
    for j in range(X - c + 1):
        if dp[j] != INF:
            dp[j + c] = min(dp[j + c], dp[j] + 1)

result = dp[X] if dp[X] != INF else -1
print(result)
