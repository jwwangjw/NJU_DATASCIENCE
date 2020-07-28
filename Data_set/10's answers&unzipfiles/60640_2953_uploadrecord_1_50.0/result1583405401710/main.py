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
for i in range(1, n):
    cnt = 0
    if gcd(n, i) == 1:
        ans = min(ans, cnt-1)
print(ans, end="")
