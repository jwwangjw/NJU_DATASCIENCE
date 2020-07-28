class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        houses.sort()
        heaters.sort()
        l1 = len(heaters)
        l2 = len(houses)
        if l1 == 1:
            return max(abs(houses[0] - heaters[0]), abs(houses[-1] - heaters[0]))
        res = 0
        j = 0
        m = l2 - 1
        while m >= 0 and houses[m] >= heaters[-1]:
            m -= 1
        if m != l2 - 1:
            res = houses[-1] - heaters[-1]
        n = 0
        while n < l2 and houses[n] <= heaters[0]:
            n += 1
        if n != 0:
            res = max(res, heaters[0] - houses[0] )
        for i in range(n, m + 1):
            while houses[i] > heaters[j]:
                j += 1
            if houses[i] == heaters[j]:
                continue
            res = max(res, min(houses[i] - heaters[j - 1], heaters[j] - houses[i]))
        return res
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))

s = Solution()
print(s.findRadius(c1,c2))
