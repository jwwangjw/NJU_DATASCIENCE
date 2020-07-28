n=int(input())
name=[]
scores=[]
allscores=[]
#name中储存n轮得分人的姓名，scores储存n轮的得分情况，两者一一对应
for i in range(n):
    string=input().split(" ")
    name.append(string[0])
    scores.append(int(string[1]))
namesingle=list(set(name))
#namesingle中存储所有人姓名，分别计算每个人总分，存储在allscores中
for i in range(len(namesingle)):
    index=[k for k,v in enumerate(name) if v==namesingle[i]]
    score=0
    for j in index:
        score+=scores[j]
    allscores.append(score)
m=max(allscores)
#若最高分只有一人，胜利者就是他
if allscores.count(m)==1:
    print(namesingle[allscores.index(m)])
#若最高分不止一人，则回头找谁得分最高,situation中储存情况
else:
    situation = []
    for i in range(len(namesingle)):
        situation.append(0)
    i = 0
    while not m in situation:
        place=namesingle.index(name[i])
        situation[place]+=scores[i]
        i+=1
    print(namesingle[place])
