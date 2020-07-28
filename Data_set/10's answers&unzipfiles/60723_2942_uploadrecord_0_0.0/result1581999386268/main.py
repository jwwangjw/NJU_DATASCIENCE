def input_manage():
    string=input()
    array=string.split(" ")
    return array
number=int(input())
array=input_manage()
array=sorted(array,key= lambda i:i[0])
print(int(''.join(array)))