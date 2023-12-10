MODULO = 0


def setup(testing):
    global MODULO
    global dp
    global coins
    global desiredSum
    if testing == False:
        l1 = input().split()
        l2 = input().split()
    else:
        l1 = "3 9".split()
        l2 = "2 3 5".split()
    MODULO = 10**9 + 7

    coins = []
    x = int(l1[0])
    desiredSum = int(l1[1])

    for i in range(x):
        coins.append(int(l2[i]))

    dp = [0] * (desiredSum + 1)
    dp[0] = 1


setup(False)

for coin in coins:
    for i in range(desiredSum - coin + 1):
        if dp[i] == 2 and i > 990:
            a = 2
        dp[i + coin] += dp[i]
        dp[i] = dp[i] % MODULO
print(dp[-1])
