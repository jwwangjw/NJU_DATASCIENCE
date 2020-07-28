A=eval(input())
result=[]
for i in range(len(A),0,-1):
    max_index=A[:i].index(max(A[:i]))
    if max_index!=i-1:
        A[:max_index-1]=A[:max_index][::-1]
        A[:i]=A[:i][::-1]
        result.extend([max_index+1,i])
if len(result)==2:
    print(result[1:])
else:
    print(result)