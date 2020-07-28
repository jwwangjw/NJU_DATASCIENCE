import  collections
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res, m, maxl = 0, collections.Counter(), 0
        for i in range(len(s)):
            m[s[i]] += 1
            maxl = max(maxl, m[s[i]])
            if res - maxl < k:
                res += 1
            else:
                m[s[i - res]] -= 1
        return res
b = input()
a = int(input())
s = Solution()
print(s.characterReplacement(b,a))