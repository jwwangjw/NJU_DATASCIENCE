start=input()
end=input()
wordList=eval(input())
class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        from collections import defaultdict
        if endWord not in wordList: return []
        forward,backward,wordList,dic = {beginWord},{endWord},set(wordList),defaultdict(set)
        flag,letters,length = True,set('qwertyuioplkjhgfdsazxcvbnm'),len(endWord)
        while forward:
            if len(forward) > len(backward):
                forward,backward,flag = backward,forward,not flag
            cur = set()
            wordList -= forward
            for word in forward:
                for idx in range(length):
                    x,y = word[:idx],word[idx+1:]
                    for letter in letters:
                        temp = x + letter + y
                        if temp in wordList:
                            cur.add(temp)
                            if flag: dic[temp].add(word)
                            else: dic[word].add(temp)
            if cur & backward:
                res = [[endWord]]
                while res[0][0] != beginWord:
                    res = [[x]+y for y in res for x in dic[y[0]]]
                return res
            forward = cur
        return []
s=Solution()
res=s.findLadders(start,end,wordList)
if len(res)<=1:
    print(res)
else:
    print("[")
    for i in range(len(res)):
        print("  ", end="")
        print(res[i], end="")
        if i < len(res) - 1:
            print(",")
        else:
            print()
    print("]")