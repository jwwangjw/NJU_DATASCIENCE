class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        a, b, P, S = A, B, A * B, A + B
        while a:
            a, b = b % a, a
        d, r = N // (S // b - 1), N % (S // b - 1)
        return (d * P // b + (P * r + min((-B * r) % S * A, (-A * r) % S * B)) // S) % 1000000007
a = int(input())
b = int(input())
c = int(input())
s = Solution()
print(s.nthMagicalNumber(a,b,c))