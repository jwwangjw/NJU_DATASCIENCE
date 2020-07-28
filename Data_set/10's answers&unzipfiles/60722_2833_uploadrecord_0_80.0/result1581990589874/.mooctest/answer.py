n = int(input())
a = sum(map(int, input().split()))
b = sum(sorted(map(int, input().split()))[-2:])
print("YES" if b >= a else "NO")
