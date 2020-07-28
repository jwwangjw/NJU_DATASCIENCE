n=int(input())
score=input().split(" ")
for i in range(n):
    score[i]=int(score[i])
score.sort()
new=score[0]
if new!=0:
    num=1
else:
    num=0
for i in range(n):
    if score[i]>0 and score[i]!=new:
        num=num+1
    new=score[i]
print(num)