import random

count = 0

uniqueCombos = []


desiredSum = int(input())

for i in range(10000):
    curTry = []
    while sum(curTry) < desiredSum:
        curTry.append(random.randint(1, 2))
    if sum(curTry) == desiredSum and curTry not in uniqueCombos:
        uniqueCombos.append(curTry)

uniqueCombos.sort()

for i in range(len(uniqueCombos)):
    print("===================")
    print(f"Combo {i}: {uniqueCombos[i]}")

print("===================")
print(f"Total combos: {len(uniqueCombos)}")
