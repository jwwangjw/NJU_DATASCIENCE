for _ in range(int(input())):
    a=input()
    n=len(a)
    arr=[1 for i in range(n)]
    for i in range(n):
        for j in range(i):
            if ord(a[i])>ord(a[j]):
                arr[i]=max(arr[i],arr[j]+1)
    print(max(arr))