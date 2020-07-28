from collections import defaultdict
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        mem = defaultdict(int)
        for char in t:
        	mem[char]+=1
        t_len = len(t)

        minLeft, minRight = 0,len(s)
        left = 0

        for right,char in enumerate(s):
        	if mem[char]>0:
        		t_len-=1
        	mem[char]-=1

        	if t_len==0:
        		while mem[s[left]]<0:
        			mem[s[left]]+=1
        			left+=1

        		if right-left<minRight-minLeft:
        			minLeft,minRight = left,right

        		mem[s[left]]+=1
        		t_len+=1
        		left+=1
        return '' if minRight==len(s) else s[minLeft:minRight+1]

a = input()
b = input()

s = Solution()
print(s.minWindow(a,b))