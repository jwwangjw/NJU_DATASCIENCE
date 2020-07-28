stones=input().split(",")
for i in range(len(stones)):
    stones[i]=int(stones[i])
stones.sort()
i, n = 0, len(stones)
min_moves = n
max_moves = max(stones[-1]-stones[1], stones[-2]-stones[0])-n+2
for j in range(n):
    while stones[j]-stones[i] >= n:
        i += 1
    if j-i+1 == n-1 and stones[j]-stones[i]==n-2:
        min_moves = min(2, min_moves)
    else:
        min_moves = min(min_moves, n-(j-i+1))
print([min_moves, max_moves])