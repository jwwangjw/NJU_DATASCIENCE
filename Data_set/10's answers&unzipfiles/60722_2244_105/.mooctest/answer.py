class Solution:
    def primePalindrome(self, N: int) -> int:
        if N == 1:
            return 2

        while self.IsHuiWenShu(N) == False or self.IsSushu(N) == False:
            if N > 11 and len(str(N)) % 2 == 0:
                N = 10 ** len(str(N)) + 1
            else:
                N = N + 1
        return N

    def IsSushu(self, A):
        for i in range(2, int(A ** 0.5) + 1):
            if A % i == 0:
                return False
        return True

    def IsHuiWenShu(self, B):
        str_B = str(B)
        if str_B != str_B[::-1]:
            return False
        return True
a = int(input())
s = Solution()
print(s.primePalindrome(a))