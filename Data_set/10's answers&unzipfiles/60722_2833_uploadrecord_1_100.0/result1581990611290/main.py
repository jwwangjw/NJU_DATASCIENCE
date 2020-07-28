n=int(input())
volume=input().split(" ")
cap=input().split(" ")
num=0
for i in range(n):
    num+=int(volume[i])
    cap[i]=int(cap[i])
cap.sort()
cap.reverse()
if num<=(cap[0]+cap[1]):
    print("YES")
else:
    print("NO")
