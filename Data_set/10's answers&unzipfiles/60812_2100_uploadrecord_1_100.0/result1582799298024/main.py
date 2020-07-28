n = 1
for i in range(1, int(input())+1):
    n *= i
a = b = 0
while n % 2 == 0:
    n /= 2
    a += 1
while n % 5 == 0:
    n /= 5
    b += 1
print(min(a, b))