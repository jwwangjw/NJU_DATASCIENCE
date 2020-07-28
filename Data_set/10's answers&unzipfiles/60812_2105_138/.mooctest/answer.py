class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        return (C-A)*(D-B)+(H-F)*(G-E)-max(0,min(C-E,G-A,G-E,C-A))*max(0,min(H-F,D-B,H-B,D-F))
s= input().split(',')

d = Solution()
print(d.computeArea(int(s[0]),int(s[1]),int(s[2]),int(s[3]),int(s[4]),int(s[5]),int(s[6]),int(s[7])))
