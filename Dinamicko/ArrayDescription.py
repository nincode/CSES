MODULO = 10**9 + 7

l1 = input().split()

len_arr = int(l1[0])
max_val = int(l1[1])

l2 = input().split()

arr = []

for i in range(len_arr):
    arr.append(int(l2[i]))


class Tree:
    def __init__(self, data, depth, maxDepth, end_val) -> None:
        self.left = None
        self.right = None
        self.mid = None
        self.data = data
        self.depth = depth
        self.maxDepth = maxDepth
        self.end_val = end_val

    def main(self):
        combos = 0
        possibilitties = []
        if self.data - 1 > 0:
            possibilitties.append(self.data - 1)
        possibilitties.append(self.data)
        if self.data + 1 < max_val:
            possibilitties.append(self.data + 1)

        if self.depth == self.maxDepth - 1:
            if abs(self.data - self.end_val) <= 1:
                return 1
            return 0
        self.left = Tree(possibilitties[0], self.depth + 1, self.maxDepth, self.end_val)
        combos += self.left.main()
        if len(possibilitties) > 1:
            self.mid = Tree(
                possibilitties[1], self.depth + 1, self.maxDepth, self.end_val
            )
            combos += self.mid.main()
        if len(possibilitties) > 2:
            self.right = Tree(
                possibilitties[2], self.depth + 1, self.maxDepth, self.end_val
            )
            combos += self.right.main()

        return combos


global_combos = 0
for i in range(len_arr):
    if i + 1 < len_arr:
        if arr[i + 1] == 0:
            nextZero = 0
            end_vali = 0

            for j in range(i + 1, len_arr - i):
                if arr[j] == 0:
                    nextZero = j
                    if j + 1 < len_arr:
                        end_vali = arr[j + 1]
                    else:
                        end_vali = 0
                    break

            root = Tree(arr[i], i, nextZero + 1, end_vali)
            global_combos += root.main()


print(global_combos % MODULO)
