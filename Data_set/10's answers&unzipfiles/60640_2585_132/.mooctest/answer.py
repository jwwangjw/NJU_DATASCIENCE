class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        s = start.replace('X', '')
        e = end.replace('X', '')
        if s != e:
            return False
        last_start, last_end = 0, 0
        for i in s:
            s_index = start.index(i, last_start)
            e_index = end.index(i, last_end)
            if (i == 'L' and s_index >= e_index) or (i == 'R' and s_index <= e_index):
                last_start = s_index + 1
                last_end = e_index + 1
            else: return False
        return True
a = input()
b = input()
s = Solution()
print(s.canTransform(a,b))