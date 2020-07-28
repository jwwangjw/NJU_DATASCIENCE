differ=[]
string=input()
num=0
for i in range(len(string)):
    if string.count("2",0,i+1)<string.count("5",0,i+1):
        num=-1
    else:
        differ.append(abs(string.count("2",0,i+1)-string.count("5",0,i+1)))
if num!=-1:
    num=max(differ)
print(num)