s=input()
swap=input()
swapp=[]
i=2
while i<len(swap):
    swapp.append(swap[i:i+3])
    i+=6
for i in range(len(s)):
    sett=[]
    sett.append(s[i:i+1])
    for j in range(len(swapp)):
        choice=swapp[j]
        place=choice.split(",")
        placel=int(place[0])
        placer=int(place[1])
        if s[placel:placel+1] in sett:
            sett.append(s[placer:placer+1])
        if s[placer:placer+1] in sett:
            sett.append(s[placel:placel+1])
    sett=list(set(sett))
    sett.sort()
    k=0
    while k<len(sett):
        for m in range(len(s)):
            if s[m:m+1] in sett:
                s=s[:m]+sett[k]+s[m+1:]
                k+=1
print(s)
