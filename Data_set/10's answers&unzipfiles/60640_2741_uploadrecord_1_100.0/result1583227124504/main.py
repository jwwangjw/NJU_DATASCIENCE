inp = eval(input())
max_len = 1
curr_len = 1
for i in range(len(inp)-1):
    if inp[i] < inp[i+1]:
        curr_len += 1
    else:
        max_len = max(max_len, curr_len)
        curr_len = 1
max_len = max(max_len, curr_len)
print(max_len)
