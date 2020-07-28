from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        s0 = Solution()
        aa = s0.merge1(intervals)
        return aa

    def merge1(self, a):
        s1 = Solution()
        ok = True
        for i in a:
            for j in a:
                if i == j:
                    continue
                else:
                    if i[0] <= i[1] < j[0] <= j[1] or j[0] <= j[1] < i[0] <= i[1]:
                        continue
                    else:
                        ok = False
                        a.remove(i)
                        a.remove(j)
                        result = [min(i[0], j[0]), max(i[1], j[1])]
                        a.append(result)
                        break
            if not ok:
                break
        if not ok:
            return s1.merge1(a)
        if ok:
            b = sorted(a, key=lambda x: x[0])
            for l in b:
                if b.count(l) != 1:
                    for x in range(0, b.count(l) - 1):
                        b.remove(l)
            return b


if __name__ == '__main__':
    s = Solution()
    a = eval(input())
    print(s.merge(a))
def merge(a):
    ok = True
    for i in a:
        for j in a:
            if i == j:
                continue
            else:
                if i[0] < i[1] < j[0] < j[1] or j[0] < j[1] < i[0] < i[1]:
                    continue
                else:
                    ok = False
                    a.remove(i)
                    a.remove(j)
                    result = [min(i[0], j[0]), max(i[1], j[1])]
                    a.append(result)
                    break
        if not ok:
            break
    if not ok:
        merge(a)
    if ok:
        a.sort(key=lambda x: x[0])
        print(a)


if __name__ == '__main__':
    a = eval(input())
    merge(a)
