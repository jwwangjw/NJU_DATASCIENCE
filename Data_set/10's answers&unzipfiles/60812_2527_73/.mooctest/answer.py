restaurants = eval(input())
veganFriendly = int(input())
maxPrice = int(input())
maxDistance = int(input())
for rest in restaurants:
    if veganFriendly and not rest[2]:
        rest[1]=0
    elif maxPrice<rest[3] or maxDistance<rest[4]:
        rest[1]=0
restaurants.sort(key=lambda x:[x[1],x[0]],reverse=True)
a = []
for rest in restaurants:
    if rest[1]:
        a.append(rest[0])
print(a)
