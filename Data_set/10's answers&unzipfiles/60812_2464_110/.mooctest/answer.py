class Solution:
    def minSubArrayLen(self, s: int, nums) -> int:
        left, right, res = 0, len(nums), 0
        def helper(size):
            sum_size = 0
            for i in range(len(nums)):
                sum_size += nums[i]
                if i >= size:
                    sum_size -= nums[i-size]
                if sum_size >= s:
                    return True
            return False
        while left<=right:
            mid = (left+right)//2  # 滑动窗口大小
            if helper(mid):  # 如果这个大小的窗口可以那么就缩小
                res = mid
                right = mid-1
            else:  # 否则就增大窗口
                left = mid+1
        return res
a = int(input())
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.minSubArrayLen(a,c))