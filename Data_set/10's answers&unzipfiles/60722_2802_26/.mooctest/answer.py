import queue
n, m = map(int, input().split())
q = queue.Queue(n)
for i, x in enumerate(map(int, input().split()), 1):
    q.put([i, x])
a = [0, 0]
while not q.empty():
    a = q.get()
    if a[1] > m:
        a[1] -= m
        q.put(a)

print(a[0])
