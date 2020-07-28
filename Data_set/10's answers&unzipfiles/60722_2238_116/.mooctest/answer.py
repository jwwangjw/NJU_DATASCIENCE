class Solution:
    def numRabbits(self, answers) -> int:
        s = 0
        temp = {}
        for i in answers:
            if 0==i:
                s+=1
            elif temp.get(i):
                temp[i] += 1
            else:
                temp[i] = 1
        for i in temp.keys():
            if temp[i] > i+1:
                s += temp[i]//(i+1)*(i+1)+i+1 if 0!=temp[i]%(i+1) else temp[i]//(i+1)*(i+1)
            else:
                s += i+1
        return s
b = input().split(',')
c= []
for i in b:
    c.append(int(i))
s = Solution()
print(s.numRabbits(c))