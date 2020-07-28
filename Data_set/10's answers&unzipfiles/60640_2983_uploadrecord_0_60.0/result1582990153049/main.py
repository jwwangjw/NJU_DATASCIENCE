"""
对于不可能的情况
1. 字符串长度为奇数，出现次数为奇数的字符数量超过1
2. 字符串长度为偶数，出现次数为奇数的字符数量超过0
采用贪心法
start，end
对于前半段字符串的每个字母，从尾部开始找到第一个和它相同的字母，计算所需要的移动次数，并移动
不断缩小范围，直到start>=end
"""
n = int(input())
s = list(input())
start = 0
end = n-1
count_odd = 0
ans = 0
for start in range(end):
    for j in range(end, start-1, -1):
        # 出现次数为奇数的字符
        if start == j:
            count_odd += 1
            if n % 2 == 0 or count_odd > 1:
                print("Impossible")
                exit()
            ans += n//2-start
            break
        elif s[j] == s[start]:
            ans += end-j
            for f in range(j, end):
                s[f] = s[f+1]
            s[end] = s[start]
            end -= 1
            break
print(ans)
