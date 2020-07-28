class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        point1=0
        point2=0
        while point1<len(s) and point2<len(t):
            if s[point1]!=t[point2]:
                point2+=1
            else:
                point1+=1
                point2+=1
        if point1==len(s):return True
        return False
a = input()
b = input()
s = Solution()
print(s.isSubsequence(a,b))