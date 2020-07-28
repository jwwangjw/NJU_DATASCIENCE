str1=input()
str2=input()
if len(str1)!=len(str2):
    print(1)
else:
    if str1==str2:
        print(2)
    elif str1.lower()==str2.lower():
        print(3)
    else:
        print(4)