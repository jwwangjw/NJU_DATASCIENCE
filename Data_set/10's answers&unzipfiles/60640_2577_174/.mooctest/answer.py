import itertools
import heapq
class Solution:
    def jobScheduling(self, startTime, endTime, profit) -> int:
        H = sorted(zip(startTime, itertools.repeat(1), endTime, profit))
        res = 0
        while H:
            t = heapq.heappop(H)
            if t[1]:
                heapq.heappush(H, (t[2], 0, res + t[3]))
            else:
                res = max(res, t[2])
        return res
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
b3 = input().split(',')
c3= []
for i in b3:
    c3.append(int(i))
s = Solution()
print(s.jobScheduling(c1,c2,c3))