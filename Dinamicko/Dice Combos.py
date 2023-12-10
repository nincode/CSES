maxLen = 10 ** 6
theMOD = 10 ** 9+7
dp = []

n = int(input())
for i in range(n+1):
    dp.append(0)
dp[0] = 1

for i in range(1,n+1):
    for j in range(1,7):
        if i-j <0:
            break
        dp[i] = (dp[i] + dp[i-j]) % theMOD

print(dp[n])
