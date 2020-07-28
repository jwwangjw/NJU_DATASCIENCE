n = int(input())


def f(x):
    x = int(x)
    for i in (2, 3):
        while x > 0 and x % i == 0:
            x //= i
    return x


s = set(map(f, input().split()))
print('Yes' if len(s) == 1 else 'No')
