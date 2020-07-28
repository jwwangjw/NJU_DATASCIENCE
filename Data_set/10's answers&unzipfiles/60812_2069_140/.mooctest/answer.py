class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """
        思路：123*89 = (9*3*1 + 9*2*10 + 9*1*100)*1 + (8*3*1 + 8*2*10 + 8*1*100)*10
        """
        res = 0
        count2 = 1
        for n2 in num2[::-1]:
            count1 = 1
            for n1 in num1[::-1]:
                res += (int(n2)*int(n1)*count1)*count2
                count1 *= 10
            count2 *= 10
        return str(res)
a = input()
b = input()
s = Solution()
print(s.multiply(a, b))
