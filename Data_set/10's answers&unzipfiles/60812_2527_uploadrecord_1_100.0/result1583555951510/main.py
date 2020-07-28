a = list(eval(input()))
veganfriendly = int(input())
maxprice = int(input())
maxdistance = int(input())
for i in a[:]:
    if i[2] < veganfriendly or i[3] > maxprice or i[4] > maxdistance:
        a.remove(i)
id = []
for i in sorted(a, key=lambda x:(x[1], x[0]), reverse=True):
    id.append(i[0])
print(id)