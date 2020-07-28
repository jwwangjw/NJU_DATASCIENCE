import functools
import operator


for t in range(int(input())):
    input()
    s = int(input().replace(' ', ''))%3
    if s == 0:
        print(1)
    else:
        print(0)
    