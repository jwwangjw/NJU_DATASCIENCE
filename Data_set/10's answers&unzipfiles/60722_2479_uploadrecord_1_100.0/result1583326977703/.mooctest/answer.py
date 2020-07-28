T=int(input())
for i in range(T):
    s1=input()
    s2=input()
    set1=set()
    set2=set()
    for i in s1:
        set1.add(i)
    for i in s2:
        set2.add(i)
    a=set1.difference(set2)
    b=set2.difference(set1)
    c=a.union(b)
    d=sorted(list(c))
    print(''.join(d))
print()