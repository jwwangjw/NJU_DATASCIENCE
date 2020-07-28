prime=[]
arr=[1]*50000
arr[0]=0
arr[1]=0
for i in range(2,50000):
    for j in range(2,int(i**.5)+1):
        if i%j==0:
            arr[i]=0
for i in range(0,50000):
    if arr[i]==1:
        prime.append(i)
#findseries(n,prime)
#print(len(prime))
for i in range(int(input())):
    n = int(input())
    print(prime[n-1]**2+1)
    