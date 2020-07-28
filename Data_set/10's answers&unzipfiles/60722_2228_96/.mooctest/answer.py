class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        sum = 0
        i = 1
        while True:
            sum += i
            if sum>= target and (sum - target)%2==0:
                return i
            i += 1
a = input()
s = Solution()
print(s.reachNumber(int(a)))