str = input()
lists = list(str)
#print(lists)

s = ""
t = ""
index = []
for i in range(lists.__len__()):
    if lists[i] == '"':
        index.append(i)
for i in range(index[0], index[1]+1):
    s+=lists[i]
for i in range(index[2], index[3]+1):
    t+=lists[i]

#print(s)
#print(t)

lists1 = list(s)
lists1.sort()
lists2 = list(t)
lists2.sort()

if lists1 == lists2:
    print("true")
else:
    print("false")