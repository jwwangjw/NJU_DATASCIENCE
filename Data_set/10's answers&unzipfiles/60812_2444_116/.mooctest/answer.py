s=input()
s="".join(s.split(' '))
nums=[]
begin=0
end=0
k=0
t=0
for i in range(len(s)):
    if(s[i]=='['):
        begin=i
    elif(s[i]==']'):
        end=i
        nums=list(eval(s[begin:end+1]))
    elif(s[i-2]=='k'):
        tmp=0
        for z in range(i,len(s)):
            if(s[z]==','):
                tmp=z
                break
        k=int(s[i:tmp])
    elif(s[i-2]=='t'):
        t=int(s[i:])

for i in range(len(nums)-1):
    for z in range(i+1,len(nums)):
        if(abs(nums[i]-nums[z])<=t and abs(i-z)<=k):
            print('true')
            exit()
print('false')
