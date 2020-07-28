class Solution:
    def calculateMinimumHP(self, dungeon):
        m=len(dungeon)
        n=len(dungeon[0])
        dp=[[0]*n for _ in range(m)] # 创建二维dp数组
        # 下面都是边界状态，要保证血量时刻大于0
        dp[-1][-1]=max(1,1-dungeon[-1][-1]) # 右下角终点需要的最小值，若右下角为负，需要1-dungeon[-1][-1]，若为正需要1
        for i in range(n-2,-1,-1): # 最下面一行的边界
            '''
            这里有两种情况，
            1，如果当前位置需要的血dungeon[-1][i]小于等于后一个位置的最小生命
            若dungeon[-1][i]为正，那么当前位置的所需最小生命就是后一个位置dp[-1][i+1]减去dungeon[-1][i]这些血
            （dungeon[-1][i]为正相当于加血）
            若dungeon[-1][i]为负，一样的，因为当前位置还要扣血，所以需要的更多，减去负的就是加
            2，如果当前位置需要的血dungeon[-1][i]大于后一个位置的最小生命，只需要1滴血即可
            '''
            dp[-1][i]=max(1,dp[-1][i+1]-dungeon[-1][i])
        for i in range(m-2,-1,-1): # 有右边一列的边界，同上
            dp[i][-1]=max(1,dp[i+1][-1]-dungeon[i][-1])
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                # 正下方和右侧位置所需的最小生命值中的较小者，和初始化一样
                dp[i][j]=max(min(dp[i+1][j],dp[i][j+1])-dungeon[i][j],1)
        return dp[0][0]

num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)

s = Solution()
print(s.calculateMinimumHP(n))