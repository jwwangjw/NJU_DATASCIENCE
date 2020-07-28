t = int(input())
while t>0:
    n = int(input())
    w = input().split()
    d = {}
    for item in w:
      s = "".join(sorted(item))
      if s not in d.keys():
        d[s] = []
      d[s].append(item)
    input2 = list(d.values())
    #print (input2)
    m = []
    for e in input2:
        m.append(len(e))
    
    m.sort()
    print (' '.join(str(x) for x in m)) 
    t-= 1