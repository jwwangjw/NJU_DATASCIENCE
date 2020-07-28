class Solution:
    def intToRoman(self, num: int) -> str:
        rome = {
            1: 'I',
            4: 'IV',
            5: 'V',
            9: 'IX',
            10: 'X',
            40: 'XL',
            50: 'L',
            90: 'XC',
            100: 'C',
            400: 'CD',
            500: 'D',
            900: 'CM',
            1000: 'M',
        }
        compare = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        ans = ""
        i = 0
        while num != 0:
            while num >= compare[i]:
                ans += rome[compare[i]]
                num -= compare[i]
            i += 1
        return ans
a = input()
s = Solution()
print(s.intToRoman(int(a)))
