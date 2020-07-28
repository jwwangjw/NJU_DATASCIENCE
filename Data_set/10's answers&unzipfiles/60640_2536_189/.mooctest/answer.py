import ast
airport = ast.literal_eval(input())

route = []
temp = []
for i in range(airport.__len__()):
    if airport[i][0] == "JFK":
        temp.append(airport[i])
temp.sort()
start = temp[0]
route.append(start[0])
route.append(start[1])
#print("route: ", end="")
#print(route)
for j in range(airport.__len__()):
    for i in range(airport.__len__()):
        if airport[i][0] == route[route.__len__() - 1]:
            route.append(airport[i][1])
            airport[i][0] = "null"
            break
        #print("route: ", end="")
        #print(route)

print(route)