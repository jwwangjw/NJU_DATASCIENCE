class Solution:
    def superPow(self, a: int, b) -> int:
        if not b: return 1
        tmp = b.pop()
        return (((self.superPow(a, b)) ** 10) % 1337 * \
                (a ** tmp) % 1337 ) % 1337
a = int(input())
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.superPow(a,c))