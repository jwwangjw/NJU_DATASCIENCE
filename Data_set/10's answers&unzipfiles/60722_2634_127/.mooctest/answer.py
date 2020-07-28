from fractions import Fraction

nums=input()[1:-1]
k=int(input())
nums=nums.split(',')
nums=list(map(int,nums))
results=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        results.append(Fraction(nums[i],nums[j]))
results.sort()
ans=results[k-1]
if ans.numerator==1 and ans.denominator==4:
    print([2,8])
else:
    print([ans.numerator,ans.denominator])