data = eval(input())
lower = int(input())
upper = int(input())
result = []
for i in range(len(data)):
    for j in range(i+1, len(data)+1):
        if sum(data[i:j]) in range(lower, upper+1):
            result.append([i, j-1])
print(len(result))
