src=eval(input())
k=int(input())
def find(src,k):
    maxval=0
    for i in range(k):
        maxval=max(src)
        src.remove(maxval)
    return maxval
print(find(src,k))