class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        lens = len(citations) - 1
        it = 0
        for i, c in enumerate(citations):
            if i + 1 <= citations[lens - i] and it <= i + 1:
                it = i + 1

        return it
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.hIndex(c))