from collections import defaultdict
beginword=input()
endword=input()
wordlist=eval(input())
def ladderLength(beginword,endword,wordlist):
    if endword not in wordlist or not endword or not wordlist:
        return 0
    size=len(beginword)
    all_combo=defaultdict(list)
    for word in wordlist:
        for i in range(size):
            all_combo[word[:i]+"*"+word[i+1:]].append(word)
    queue=[(beginword,1)]
    visited={beginword:True}
    while queue:
        cur,level=queue.pop()
        for i in range(size):
            intermediate=cur[:i]+"*"+cur[i+1:]
            for word in all_combo[intermediate]:
                if word==endword:
                    return level+1
                if word not in visited:
                    visited[word]=True
                    queue.append((word,level+1))
            all_combo[intermediate]=[]
    return 0
print(ladderLength(beginword,endword,wordlist))
