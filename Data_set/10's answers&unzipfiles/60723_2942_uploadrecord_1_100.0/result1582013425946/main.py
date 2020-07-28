def input_manage():
    string=input()
    array=string.split(" ")
    array.sort(reverse=True)
    return array
number=int(input())
array=input_manage()
print(int(''.join(array)),end='')