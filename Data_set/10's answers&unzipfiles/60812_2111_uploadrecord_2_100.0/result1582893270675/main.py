n = int(input())
l = [2,3,5]
count = 1
num = 2
while count < n:
    temp = num
    for j in l:
        while temp % j == 0:
            temp //= j
    if temp == 1:
        count += 1
    num += 1
print(num-1)