def number(num):
    return ((num)**3 + (num))
    
T = int(input())
for t in range(T):
    n = int(input())
    print(str(number(n)))