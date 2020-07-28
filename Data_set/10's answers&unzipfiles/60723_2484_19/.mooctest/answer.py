for i in range(int(input())):
    n,m = (int(i) for i in input().split())
    arr = list(map(int,input().strip().split()))
    arr2 = list(map(int,input().strip().split()))
    s=set(arr+arr2)
    print(len(s))