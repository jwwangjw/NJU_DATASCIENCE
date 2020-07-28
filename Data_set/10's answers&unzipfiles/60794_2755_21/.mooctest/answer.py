
def mulPoly(l1, l2):
    s = [0] * (len(l1)+len(l2)-1)
    for k, i in enumerate(l2):
        n = k
        for j in l1:
          m = i*j
          s[n] = s[n] + m
          n = n+1
    print(" ".join([str(x) for x in s]))

t = int(input())
for i in range(0, t):
    n = input()
    l1 = list(map(int, list(input().split())))
    l2 = list(map(int, list(input().split())))
    mulPoly(l1, l2)