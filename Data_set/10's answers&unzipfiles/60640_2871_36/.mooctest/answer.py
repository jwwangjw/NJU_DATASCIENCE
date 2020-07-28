n = int(input())
a1 = input().count('1')
a2 = n - a1
print(a2+(a1-a2)//3 if a2 <= a1 else a1)
