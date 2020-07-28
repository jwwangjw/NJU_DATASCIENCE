class Solution:
    def longestSubsequence(self, arr, difference):
        d = {}
        for a in arr:
            d[a] = d.get(a - difference, 0) + 1
        return max(d.values())
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
a = int(input())
s = Solution()
print(s.longestSubsequence(c,a))