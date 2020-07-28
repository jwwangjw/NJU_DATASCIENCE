for _ in range(int(input())):
    a, b = list(map(int, input().split()))
    n = int(input())
    diff = b-a
    print(a+(n-1)*diff)