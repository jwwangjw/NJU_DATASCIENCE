
import numpy as np

def calc(arr, n):
    incl = arr[0]
    excl = 0
    
    for i in range(1, n):
        incl_new = arr[i] + min(incl, excl)
        
        excl = incl
        incl = incl_new
    
    return min(incl, excl)
    
if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        arr = list(map(int, input().split()))
        print(calc(arr, n))