import math
def p(x1,y1,x2,y2):
    if x1==x2:
        return abs(y2-y1)-1
    if y2==y1:
        return abs(x2-x1)-1
    return (math.gcd(abs(y2-y1),abs(x2-x1))-1)
t=int(input())
for i in range(t):
    x1,y1=map(int,input().split())
    x2,y2=map(int,input().split())
    x3,y3=map(int,input().split())
    A =   (abs(x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2))) 
    B=p(x1,y1,x2,y2)+p(x1,y1,x3,y3)+p(x3,y3,x2,y2)+3
    print((A - B + 2) // 2 )
    
    