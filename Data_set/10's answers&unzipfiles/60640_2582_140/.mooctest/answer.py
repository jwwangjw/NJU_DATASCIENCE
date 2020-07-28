class Solution(object):
    def maxAbsValExpr(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: int
        """
        fs = [lambda x,y,i:x+y+i,lambda x,y,i:x+y-i,lambda x,y,i:x-y+i,lambda x,y,i:x-y-i]
        li = [[x,x] for x in [fs[i](arr1[0],arr2[0],0) for i in range(4)]]
        for i in range(len(arr1)):
            for k in range(4):
                t = fs[k](arr1[i], arr2[i],i)
                li[k]= max(li[k][0],t), min(li[k][1],t)
        return max(a-b for a,b in li)
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
s = Solution()
print(s.maxAbsValExpr(c1,c2))