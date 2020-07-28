class Solution(object):
    def solveEquation(self, equation):
        """
        :type equation: str
        :rtype: str
        """
        e=equation.replace('-x','-1x').replace("-","+-")
        left,right=e.split('=')
        xs,vs=0,0
        for i,f in enumerate(e.split('=')):
            if f[:1]!='+':f='+'+f
            f=f.replace('+x','+1x')
            for t in f.split('+'):
                if len(t)==0:continue
                if 'x' in t:
                    xs+=(1-2*i)*int(t[:len(t)-1])
                else:
                    vs-=(1-2*i)*int(t)
        if xs!=0:return 'x='+str(vs/xs)
        if vs==0:return "Infinite solutions"
        return "No solution"
a = input()
s = Solution()
print(s.solveEquation(a))