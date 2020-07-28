def makeDistinct(s):
    count=0
    str1=""
    for char in s:
        if char not in str1:
            str1=str1+char
            
            
        else:
            count=count+1;
    return count            
                
num = int(input())
for i in range(num):
    s=input()
    print(makeDistinct(s))
                