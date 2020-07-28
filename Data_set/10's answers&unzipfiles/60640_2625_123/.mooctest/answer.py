class Solution:
    def addOperators(self, num: str, target: int) :
        res = []
        # 参数列表， 位置， 之前输出， 之前综合， 前一个数
        def helper(index, preOutStr, preSum, preValue):
            if index == len(num):
                if preSum == target:
                    res.append(preOutStr)
                return
            # 后面的数都做乘法, 还小于前面总和
            if max(1, abs(preValue)) * (int(num[index:])) < abs(target - preSum):
                return
            for i in range(index, index + 1 if num[index] == '0' else len(num)):
                cur = num[index:i + 1]
                curValue = int(cur)
                if not preOutStr:
                    helper(i + 1, cur, curValue, curValue)
                else:
                    helper(i + 1, preOutStr + '+' + cur, preSum + curValue, curValue)
                    helper(i + 1, preOutStr + '-' + cur, preSum - curValue, -curValue)
                    helper(i + 1, preOutStr + '*' + cur, preSum - preValue + curValue * preValue, curValue * preValue)
        helper(0, '', 0, 0)
        return res
a = input()
b = int(input())
s = Solution()
print(s.addOperators(a,b))