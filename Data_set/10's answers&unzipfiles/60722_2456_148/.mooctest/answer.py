data = eval(input())
result = []
for i in range(len(data)):
    count = 0
    if i == len(data)-1:
        result.append(0)
    else:
        for j in range(i+1,len(data)):
            if data[j] < data[i]:
                count += 1
        result.append(count)
print(result)
