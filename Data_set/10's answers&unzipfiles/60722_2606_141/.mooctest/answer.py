def solve():
    nums=list(map(int,input()[1:-1].split(',')))
    target=int(input())
    for i in range(len(nums)):
        if target==nums[i]:
            return i
    return -1

if  __name__ == '__main__' :
    print(solve())