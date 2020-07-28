src=eval(input())
num_set=set(src)
longest=0

for num in num_set:
    curr = 0
    if num-1 not in num_set:
        curr+=1
        while num+1 in num_set:
            num=num+1
            curr+=1
    longest=max(longest,curr)
print(longest)