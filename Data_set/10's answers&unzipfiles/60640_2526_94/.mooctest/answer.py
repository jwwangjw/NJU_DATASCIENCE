arr1 = list(map(str, input()[1:-1].split(',')))
arr2 = list(map(str, input()[1:-1].split(',')))
result = arr1 + arr2
while result.count('null') != 0:
    result.remove('null')
final = []
for i in result:
    try:
        final.append(int(i))
    except ValueError as e:
        pass
print(sorted(final))
