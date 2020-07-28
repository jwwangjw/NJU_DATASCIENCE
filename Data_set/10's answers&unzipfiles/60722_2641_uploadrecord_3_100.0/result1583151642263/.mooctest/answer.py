class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def check12(d1,d2):    #判断d1,d2里的字频是否相同
            for x in d1.keys():
                if x not in d2:return False
                if d1[x]!=d2[x]:return False
            return True


        if len(s2)<len(s1):return False
        d1,d2={},{}
        for x in s1:
            d1[x]=d1.get(x,0)+1

        i,j=0,len(s1)
        for x in s2[i:j]:
            d2[x]=d2.get(x,0)+1
        if check12(d1,d2):return True

        while j<len(s2):
            d2[s2[i]]-=1
            i+=1
            j+=1
            d2[s2[j-1]]=d2.get(s2[j-1],0)+1
            if check12(d1,d2):return True
        return False
a = input()
b = input()

s = Solution()
print(s.checkInclusion(a,b))