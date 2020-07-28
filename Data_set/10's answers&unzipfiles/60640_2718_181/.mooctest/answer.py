string=[c for c in input()]
pairs=eval(input())
used=[]
ans=["0"]*len(string)
pairs.sort(key=lambda x:x[0])
def fill(ans,arr,pos):
    temp=[]
    for p in pos:
        temp.append(arr[int(p)])
    temp.sort()
    pos.sort()
    for i in range(len(pos)):
        ans[pos[i]]=temp[i]
while len(used)<len(pairs):
    for i in range(len(pairs)):
        if i not in used:
            temp=[pairs[i][0],pairs[i][1]]
            used.append(i)
            for j in range(i+1,len(pairs)):
                if pairs[j][0] in temp:
                    temp.append(pairs[j][1])
                    used.append(j)
                elif pairs[j][1] in temp:
                    temp.append(pairs[j][0])
                    used.append(j)
            fill(ans,string,temp)
print("".join(ans))