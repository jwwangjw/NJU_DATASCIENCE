for _ in range(int(input())):
    n = int(input())
    arr = [int(i) for i in input().split()]
    left, right = [arr[0]], [0] * n
    right[n-1] = arr[-1]
    for elem in arr[1:]:
        left.append(max(left[-1], elem))
    for idx in range(len(arr)-2, -1, -1):
        right[idx] = max(arr[idx], right[idx+1])
    water = 0
    for i in range(1, n-1):
        water_to_be_added = min(left[i-1], right[i]) - arr[i]
        if water_to_be_added > 0:
            water += water_to_be_added
    print(water)