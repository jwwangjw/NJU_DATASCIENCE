class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        binary = str(bin(N)[2:])
        res = []
        for i in binary:
            if i == '1':
                res.append('0')
            else:
                res.append('1')
        strRes = '0b' + ''.join(res)
        return int(strRes, 2)
a = int(input())
s = Solution()
print(s.bitwiseComplement(a))