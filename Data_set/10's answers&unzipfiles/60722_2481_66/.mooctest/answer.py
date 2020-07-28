


def calc(arr1, arr2):
    d = {}
    arr1 = set(arr1)
    arr2 = set(arr2)
    
    for x in arr1:
        d[x] = 1
    for x in arr2:
        d[x] = d.get(x, 0) + 1
    
    # print(d)
    
    return len([k for k, v in d.items() if v == 2])

if __name__ == '__main__':
    for _ in range(int(input())):
        m, n = map(int, input().split())
        arr1 = list(map(int, input().split()))
        arr2 = list(map(int, input().split()))
        
        print(calc(arr1, arr2))