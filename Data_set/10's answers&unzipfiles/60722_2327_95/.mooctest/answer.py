class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        left = 0
        right = len(S)
        A = []
        for i in S:
            if i == 'I':
                A.append(left)
                left += 1
            else:
                A.append(right)
                right -= 1
        A.append(right)
        return A
a = input()
s = Solution()
print(s.diStringMatch(a))