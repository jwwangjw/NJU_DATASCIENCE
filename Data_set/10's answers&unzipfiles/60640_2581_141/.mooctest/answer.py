class Solution:
 def escapeGhosts(self, ghosts, target) -> bool:
        return abs(target[0])+abs(target[1])<min([abs(target[0]-g[0])+abs(target[1]-g[1]) for g in ghosts])
num = int(input().strip())
n = []
for i in range(num):
    b = input().split(',')
    c = []
    for i in b:
        c.append(int(i))
    n.append(c)
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))
s = Solution()
print(s.escapeGhosts(n,c1))
