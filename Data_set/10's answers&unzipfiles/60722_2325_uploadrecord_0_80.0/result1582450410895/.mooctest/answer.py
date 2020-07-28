class Solution(object):
    def hasGroupsSizeX(self, deck):
        # 统计各个数出现的次数
        d = {}
        for i in range(len(deck)):
            if deck[i] in d:
                d[deck[i]] += 1
            else:
                d[deck[i]] = 1
        gcd = d[deck[0]]
        num = set(d.values())

        # 寻找最大公约数
        for i in num:
            gcd = find_gcd(gcd, i)
        if gcd == 1:
            return False
        else:
            return True


# 寻找最大公约数
def find_gcd(a, b):
    if a < b:
        a, b = b, a
    while b != 0:
        a, b = b, a % b
    return a

b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.hasGroupsSizeX(c))