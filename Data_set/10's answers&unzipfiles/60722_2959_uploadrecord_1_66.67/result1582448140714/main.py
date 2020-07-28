s1=input()
s2=input()
sub_s1=[]
sub_s2=[]
for i in range(len(s1)):
    for j in range(i+1,len(s1)+1):
        sub_s1.append(s1[i:j])
for i in range(len(s2)):
    for j in range(i+1,len(s1)+1):
        sub_s2.append(s2[i:j])
new_sub_s1=list(set(sub_s1))
num=0
for i in range(len(new_sub_s1)):
    num1=sub_s1.count(new_sub_s1[i])
    num2=sub_s2.count(new_sub_s1[i])
    num=num+num1*num2
print(num)