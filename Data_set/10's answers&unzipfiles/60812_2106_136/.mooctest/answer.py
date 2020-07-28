class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        operator = 1
        res = 0
        num = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(res)
                stack.append(operator)
                res = 0
                operator = 1
                num = 0

            elif s[i] == ')':
                res = res + num * operator
                operator = stack.pop()
                res = stack.pop() + res * operator
                num = 0
                operator = 1

            elif s[i] == '+':
                res = res + num * operator
                num = 0
                operator = 1
            elif s[i] == '-':
                res = res + num * operator
                num = 0
                operator = -1

            elif s[i] != ' ':
                num = num * 10 + int(s[i])
        res = res + num * operator
        return res
a = input()
s = Solution()
print(s.calculate(a))
