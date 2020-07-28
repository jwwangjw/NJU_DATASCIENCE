arr = eval(input())
n = len(arr)
ans = []
while n>1:
    i = arr.index(n)
    if i!=0:
        ans.append(i+1)
        arr = arr[i::-1]+arr[i+1:]
    ans.append(n)
    arr = arr[n-1::-1]+arr[n:]
    n-=1
print(ans)