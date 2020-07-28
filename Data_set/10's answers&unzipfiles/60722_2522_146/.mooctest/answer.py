arr1 = eval(input())
arr2 = eval(input())
dic ={}
ans = []
for i in arr2:
    dic[i]=arr1.count(i)
    while i in arr1:
        arr1.remove(i)
arr1.sort()
for k,v in dic.items():
    ans.extend([k for i in range(v)])
ans.extend(arr1)
print(ans)