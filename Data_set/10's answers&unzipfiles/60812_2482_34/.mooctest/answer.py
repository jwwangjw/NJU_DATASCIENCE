
def main():

    for i in range(int(input())):
        n = int(input())
        d = int(input())
        
        print(int(n/d), end ='')
        
        k = n%d
        if k == 0: 
            print()
            continue
        
        i = 0
        frac = [k]
        start = -1
        
        while True:
            k = (k*10)%d
            if k == 0: break
            if k in frac:
                start = frac.index(k)
                break
            frac.append(k)
            i += 1
        
        print('.', end='')    
        for i in range(len(frac)):
            if i == start: print('(', end='')
            print(int((frac[i]*10)/d), end='')
            
        if start > -1: print(')')
        else: print()
        
        
if __name__ == '__main__':
  main()