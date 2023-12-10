n = int(input())
MODULO = 10**9 + 7
grid = []
f = False
ways = []
for i in range(n):
    a = input()
    grid.append(a)
    ways.append([0] * n)

if grid[0][0] == "*":
    print(0)
    exit()


ways[n - 1][n - 1] = 1


def getWays(y, x):
    if y >= n:
        return 0
    if x >= n:
        return 0
    if x < 0 or y < 0:
        return 0
    return ways[y][x]


x, y = n - 1, n - 1
for i in range(0, n):
    for j in range(n - i):
        if i == 0 and j == 0:
            continue
        if grid[y - i][x - i - j] == "*":
            ways[y - i][x - i - j] = 0

        else:
            ways[y - i][x - i - j] = getWays(y - i + 1, x - i - j) + getWays(
                y - i, x - i - j + 1
            )
    for j in range(n - i):
        if i == 0 and j == 0:
            continue
        if grid[y - i - j][x - i] == "*":
            ways[y - i - j][x - i] = 0

        else:
            ways[y - i - j][x - i] = getWays(y - i - j + 1, x - i) + getWays(
                y - i - j, x - i + 1
            )
    a = 2
    # x -= 1
    # y -= 1
print(ways[0][0])
