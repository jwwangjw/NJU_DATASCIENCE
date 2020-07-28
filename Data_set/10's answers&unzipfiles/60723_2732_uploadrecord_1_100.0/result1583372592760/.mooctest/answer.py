for tt in range(int(input())):
    abc = input().split()
    a = int(abc[0])
    b = int(abc[1])
    c = int(abc[2])
    print(pow(a,b,c))
# 	extra = 1
# 	while(b!=1):
# 		tmp = a%c
# 		if(b%2!=0):
# 			extra = (extra * tmp)%c
# 		a = tmp**2
# 		b = b/2

# 	print((a*extra)%c)