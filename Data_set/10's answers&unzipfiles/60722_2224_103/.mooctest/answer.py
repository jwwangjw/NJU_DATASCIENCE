class Solution:
    def maximumSwap(self, num: int) -> int:
        n = list(str(num))
        sr = sorted(n)[::-1]  # 最大数
        if sr == n: return num  # 如果原数就是最大的, 则不用交换.
        for i in range(len(n)):  #  最大数,原数比较,出现不同,就停止,找到要交换的位置
            if n[i] != sr[i]:
                idl = i  # 左边的交换 index
                break
        mx = max(n[i:])  # 右边最大的数字
        idr = len(n)-1 - n[::-1].index(mx)  # 从后往前找到最大数字的位置, 换算成正向的.
        n[idl], n[idr] = n[idr], n[idl]  # 交换
        return int("".join(n))  # 转为数字
a = input()
s = Solution()
print(s.maximumSwap(int(a)))