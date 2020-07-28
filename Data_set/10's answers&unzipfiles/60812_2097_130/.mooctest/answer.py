class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        难点在于如何判断是否是循环小数，以及找出循环节的位置
        判断是循环: 跳出while循环的时候余数为0就不是循环小数
        找出循环节的位置: 当同一个余数出现两次时，就找到了循环节
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = '-' if numerator * denominator < 0 else ''
        numerator, denominator = abs(numerator), abs(denominator)
        m, n = divmod(numerator, denominator)  # x//y,x%y
        int_part = str(m)
        if not n:
            return sign + str(m)
        decimal_part = []
        dic = {}  # 键:余数 值:出现余数的索引
        i = 0
        # 模拟除法,当余数为0或者余数在字典中有记录的时候跳出循环
        while n and n not in dic:
            dic[n] = i
            i += 1
            m, n = divmod(n * 10, denominator)
            decimal_part.append(str(m))
        if not n:  # 不是循环小数
            res = sign + int_part + '.' + ''.join(decimal_part)
        else:
            # 在循环节之前插入(
            decimal_part.insert(dic[n], '(')
            decimal_part.append(')')
            res = sign + int_part + '.' + ''.join(decimal_part)
        return res
a = input()
b = input()
s = Solution()
print(s.fractionToDecimal(int(a), int(b)))
