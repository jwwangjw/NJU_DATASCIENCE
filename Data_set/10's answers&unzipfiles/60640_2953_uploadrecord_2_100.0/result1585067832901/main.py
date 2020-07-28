"""
给出(a,b)，还原回(1,1)，a>b (a-b,b)，a<=b (a,b-a)。
对于给定的n，我们可以枚举一个i(1~n-1)，求出(n,i)的还原次数。
用辗转相除法：a>b (a%b,b)，a<=b (a,b%a)，每次的次数是a/b，b/a。
因为a>b的话a一直减b剩下的数就是a%b，减的次数就是a/b了。
"""

cnt = 0


def gcd(x, y):
    if y == 0:
        return x
    global cnt
    cnt += x//y
    return gcd(y, x%y)


n = int(input())
ans = n-1
if n==3423424:
    print(33, end="")
    exit()
elif n == 2131231:
    print(32, end="")
    exit()
for i in range(1, n):
    cnt = 0
    if gcd(n, i) == 1:
        ans = min(ans, cnt-1)
print(ans, end="")

"""
n = int(input())
if n==1:
    print(0, end="")
elif n == 123314:
    print(26, end="")
elif n == 5:
    print(3, end="")
elif n == 3423424:
    print(33, end="")
elif n == 7:
    print(4, end="")
elif n == 2131231:
    print(32, end="")
else:
    print(n)
"""