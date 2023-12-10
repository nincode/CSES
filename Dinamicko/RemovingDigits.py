n = int(input())


c = 1
while n > 9:
    s = str(n)
    maxN = 0
    for i in range(len(s)):
        if int(s[i]) > maxN:
            maxN = int(s[i])
        if maxN == 9:
            break
    n -= maxN
    c += 1

print(c)
