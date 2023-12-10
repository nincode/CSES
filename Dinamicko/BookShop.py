l1 = input().split()

n_books = int(l1[0])
budget = int(l1[1])


pagesPerCoin = []

l2 = input().split()
l3 = input().split()

prices = []

for i in range(n_books):
    pagesPerCoin.append([int(l3[i]) / int(l2[i]), int(l2[i])])

pagesPerCoin.sort(reverse=True)

i = 0

counter = 0

while True:
    val = pagesPerCoin[i][1]
    if budget - val >= 0:
        budget -= val
        counter += pagesPerCoin[i][1] * pagesPerCoin[i][0]
    i += 1
    if i == n_books:
        break
print(int(counter))
