def minSwap(row):
    count = 0
    for i in range(0, len(row) - 1, 2):
        if row[i] % 2 == 0:
            temp = row[i] + 1
        else:
            temp = row[i] - 1
        if temp == row[i + 1]:
            continue
        for j in range(i + 2,len(row)):
            if row[j] == temp:
                row[i + 1], row[j] = row[j], row[i + 1]
                count += 1
                break
    return count

row = eval(input())
print(minSwap(row))