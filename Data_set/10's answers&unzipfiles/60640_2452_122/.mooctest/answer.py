from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x_size = len(matrix)
        if not (x_size and len(matrix[0])):
            return False
        y_size = len(matrix[0])
        upper = 0
        bottom = x_size-1

        while upper <= bottom:  #循环退出的时候bottom指向的位置是恰巧小于target的那个行
            '''
            二分法，因为是两边逼近，因此进入条件一定要允许左右重叠的情况进入，意味着退出条件为左右边界错过。
            这样做的好处在于：
                1. 避免判定端点的情况了，反正端点最后要重合的，那么mid也就也重合了。因此只要判定mid就行了，不用左右端点
                2. 循环退出的时候，边界指向的位置有确定的大小关系。即left指向的是略大于target的，而right指向是略小于target的。即大小关系正好相反
            '''
            mid = int((upper+bottom)/2) #bot向着upper靠拢
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                bottom = mid-1
            else:
                upper = mid + 1
        left = 0
        right = y_size-1

        while left <= right:
            m = int((left+right)/2)
            if matrix[bottom][m] == target:
                return True
            if matrix[bottom][m] > target:
                right = m - 1
            else:
                left = m + 1
        return False
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
a = int(input())
s = Solution()
print(s.searchMatrix(n,a))
