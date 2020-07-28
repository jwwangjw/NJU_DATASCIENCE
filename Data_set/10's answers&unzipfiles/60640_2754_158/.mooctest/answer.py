class Solution(object):
    def maxDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        from collections import deque
        n = len(grid)
        queue = deque()
        dx = [1, -1, 0, 0]
        dy = [0, 0, 1, -1]
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    queue.append((i, j))
        if len(queue) == 0 or len(queue) == n * n: 
            return -1
        distance = -1 
        while queue:
            l = len(queue)
            
            for _ in range(l):
                cur = queue.popleft()
                x0, y0 = cur
                
                for k in range(4):
                    x = x0 + dx[k]
                    y = y0 + dy[k]
                    
                    if 0 <= x < n and 0 <= y < n and grid[x][y] == 0: 
                        grid[x][y] = 1
                        queue.append((x, y))
            distance += 1
        return distance
g=eval(input())
print(Solution().maxDistance(g))
