class Solution:
    def circularPermutation(self, n: int, start: int):
        def G(i):
            return i^(i>>1)
        a=[]
        for i in range(2**n):
            if G(i)==start:
                k=i
            a.append(G(i))
        return a[k:]+a[:k]
a = int(input())
b = int(input())
s = Solution()
print(s.circularPermutation(a,b))