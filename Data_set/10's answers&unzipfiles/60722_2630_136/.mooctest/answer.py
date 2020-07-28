import heapq

allGrids=input()[1:-1].split('],[')
allGrids[0]=allGrids[0][1:]
allGrids[len(allGrids)-1]=allGrids[len(allGrids)-1][:-1]
for i in range(len(allGrids)):
    allGrids[i]=allGrids[i].split(',')
    allGrids[i]=list(map(int,allGrids[i]))

N = len(allGrids)
seen = {(0, 0)}
gridHeap = [(allGrids[0][0], 0, 0)]
ans = 0
while gridHeap:
    d, r, c = heapq.heappop(gridHeap)
    ans = max(ans, d)
    if r == c == N-1:
        print(ans)
        break
    for cr, cc in ((r-1, c), (r+1, c), (r, c-1), (r, c+1)):
        if 0 <= cr < N and 0 <= cc < N and (cr, cc) not in seen:
            heapq.heappush(gridHeap, (allGrids[cr][cc], cr, cc))
            seen.add((cr, cc))
