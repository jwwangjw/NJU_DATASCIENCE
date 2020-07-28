
forest=[]
try:
    while True:
        temp = input()
        if temp != "[" and temp != "]":
            if temp[-1]==",":
                temp=temp[:-1]
            forest.append(eval(temp))
except EOFError:
    pass


class Solution:
    def cutOffTree(self, forest) :
        row, col = len(forest), len(forest[0])
        trees = [(forest[i][j], i, j) for i in range(row) for j in range(col) if forest[i][j] > 1]
        start = [(0, 0)]
        for i, j in start:
            for r, c in (i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1):
                if 0 <= r < row and 0 <= c < col and forest[r][c] and (r, c) not in start:
                    start.append((r, c))
        for _, i, j in trees:
            if (i, j) not in start:
                return -1

        def distance(x1, y1, x2, y2):
            base_distance = abs(x1 - x2) + abs(y1 - y2)
            trun_directions = 0
            now, next_point = [(x1, y1)], []
            visit = set()
            while True:
                if not now:
                    now, next_point = next_point, []
                    trun_directions += 1
                i, j = now.pop(0)
                if i == x2 and j == y2:
                    return base_distance + trun_directions * 2
                if (i, j) not in visit:
                    visit.add((i, j))
                    for r, c, p in (i + 1, j, i < x2), (i - 1, j, i > x2), (i, j + 1, j < y2), (i, j - 1, j > y2):
                        if 0 <= r < row and 0 <= c < col and forest[r][c]:
                            (now if p else next_point).append((r, c))

        res = 0
        trees.sort()
        if not (trees[0][1] or trees[0][2]):
            trees.pop(0)

        x1, y1, x2, y2 = 0, 0, 0, 0
        while trees:
            _, x2, y2 = trees.pop(0)
            res += distance(x1, y1, x2, y2)
            x1, y1 = x2, y2
        return res
s=Solution()
print(s.cutOffTree(forest))