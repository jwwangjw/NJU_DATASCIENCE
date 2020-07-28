for _ in range(int(input())) :
    n = int(input())

    arr1 = list(map(int,input().strip().split()))
    arr2= list(map(int,input().strip().split()))

    arr1.sort()
    arr2.sort()
    arr3=[abs(a - b) for a, b in zip(arr1,arr2)]
    print(max(arr3))