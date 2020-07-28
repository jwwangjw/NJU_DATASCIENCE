from itertools import permutations
class Solution:
    def largestTimeFromDigits(self, A):
        max_time = 0
        res = ''
        for ht,  hb, mt, mb in permutations(A):
            hour, minute = ht * 10 + hb, mt * 10 + mb
            t = hour * 60 + minute
            if hour < 24 and minute < 60 and t >= max_time:
                res = "{}{}:{}{}".format(ht, hb, mt, mb)
                max_time = t
        return res
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.largestTimeFromDigits(c))