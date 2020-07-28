#from functools import reduce
import numpy
for _ in range(int(input())):
    test_str=input()
    res = [test_str[i: j] for i in range(len(test_str)) 
          for j in range(i + 1, len(test_str) + 1)] 
    #print(res)
    l2=[]
    for i in res:
        l1=list(map(int,i))
        #result1 = reduce((lambda x, y: x * y), l1)
        result1=numpy.prod(l1)
        l2.append(result1)
    #print(l2)
    l3=[]
    flag=1
    for k in l2:
        if k in l3:
            flag=0
            print(0)
            break
        else:
            l3.append(k)
            flag=1
    if(flag==1):
        print(1)
       
            
        
        