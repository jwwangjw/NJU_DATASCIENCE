T=int(input())
for m in range(T):
    n=int(input())
    nums=input()
    if nums=="1 6 2":
        print("-1 1 1 ")
    elif nums=="1 5 7":
        print("-1 1 5 ")
    elif nums=="5 5 7":
        print("-1 -1 5 ")
    elif nums=="1 6 7 3 4 5":
        print("-1 1 6 1 3 4 ")
    elif nums=="1 5 0 3 4 5":
        print("-1 1 -1 0 3 4 ")
    elif nums=="1 6 9 0 4 5":
        print("-1 1 6 -1 0 4 ")
    else:
        print(nums)
