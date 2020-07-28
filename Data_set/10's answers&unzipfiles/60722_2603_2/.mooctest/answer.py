st1=input()
st2=st1[1:-1].split(",")
list1=list(map(int,st2))
k=int(input())
n=len(list1)*(len(list1)-1)/2
result=[]
for i in range(0,len(list1)-1):
    for j in range(i+1,len(list1)):
        result.append(abs(list1[i]-list1[j]))
result.sort()
print(result[k-1])