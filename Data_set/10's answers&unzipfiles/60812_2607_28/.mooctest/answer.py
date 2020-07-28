t=int(input())
for _ in range(t):
    s=input()
    count=0
    for i in range(len(s)):
        for j in range(i+1, len(s)):
            sub=s[i:j+1]
            if len(sub)%3==0:
                if sub.count('1')==sub.count('2')==sub.count('0'):
                    count+=1
                    
    print(count)