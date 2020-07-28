class Solution(object):
    def maxSatisfied(self, customers, grumpy, X):
        """
        :type customers: List[int]
        :type grumpy: List[int]
        :type X: int
        :rtype: int
        """
        count=0
        for i in range(len(grumpy)):
            if grumpy[i]==0:
                count=count+customers[i]
                customers[i]=0
        max=0
        i=0
        j=i+X-1
        t=i
        while t<=j:
            max=max+customers[t]
            t=t+1
        last_sum=max
        while j<len(customers)-1:
            last_sum=last_sum-customers[i]+customers[j+1]
            if last_sum>max:
                max=last_sum
            i=i+1
            j=j+1
        return(count+max)
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))
a = int(input())
s = Solution()
print(s.maxSatisfied(c,c1,a))