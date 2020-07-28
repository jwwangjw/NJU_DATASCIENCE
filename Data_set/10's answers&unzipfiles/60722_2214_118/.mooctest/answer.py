class Solution:
    def complexNumberMultiply(self, a, b):
        a = [int(s) for s in a.strip('i').split('+')]
        b = [int(s) for s in b.strip('i').split('+')]
        ans = [a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]]
        return '{}+{}i'.format(*ans)
a = input()
b = input()
s = Solution()
print(s.complexNumberMultiply(a, b))