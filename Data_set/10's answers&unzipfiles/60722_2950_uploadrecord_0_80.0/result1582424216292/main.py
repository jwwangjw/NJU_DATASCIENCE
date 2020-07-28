differ=[]
string=input()
for i in range(len(string)):
    differ.append(abs(string.count("2",0,i+1)-string.count("5",0,i+1)))
num=max(differ)
print(num)