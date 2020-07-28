def getsum(num):
  if len(str(num)) == 1:
    return num
  else :
    return getsum(sum(map(int,[i for i in str(num)])))

T = int(input())
for i in range(T):
    num = int(input())
    print(getsum(num))

    