n = int(input())
a = sorted(map(int, input().split()))
if a[n-1] - a[1] > a[n-2] - a[0]:
    print(a[n-2] - a[0])
else:
    print(a[n-1] - a[1])
