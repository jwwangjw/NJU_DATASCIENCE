class Solution(object):
    def divisorGame(self, N):
        f = [0 for i in range(N+1)]
        f[1]=0
        if N<=1: return 0
        f[2]=1
        for i in range(3,N+1):
            for j in range(1, i//2):
                if i % j == 0 and f[i-j]==0:
                    f[i] = 1
                    break
        return f[N] == 1
a = int(input())
s = Solution()
print(s.divisorGame(a))