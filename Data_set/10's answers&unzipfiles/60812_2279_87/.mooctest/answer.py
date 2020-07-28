def is_sum(a, s, n):
    start = 0
    end = 1
    mysum = a[0]
    while mysum != s:
        if mysum < s:
            if end == n:
                print -1
                return
            mysum += a[end]
            end += 1
        elif mysum > s:
            mysum -= a[start]
            start += 1
    print start + 1, end

T=int(input())
for test in range(T):
    n, s = map(int, raw_input().strip().split(' '))
    numbers = map(int, raw_input().strip().split(' '))
    is_sum(numbers, s, n)