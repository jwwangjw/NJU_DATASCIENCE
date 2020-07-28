s=input()
s=s[1:len(s)-1]
sl=s.split(',')
sum=0
for i in range(len(sl)):
    if(sl[i]=='1'):
        sum=sum+2**(len(sl)-i-1)
print(sum)