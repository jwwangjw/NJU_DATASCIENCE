def gcd(x,y):
    if y==0:return x
    return gcd(y,x%y)
def lcm(x,y):
    return x*y//gcd(x,y)
def abs(x):return x if x>0 else -x
def fracAdd(f1,d1,f2,d2):
    d = d1*d2
    f = f1*d2 + f2*d1
    g = gcd(d,f)
    d = d//g
    f = f//g
    return f,d

class Solution(object):
    def fractionAddition(self, expression):
        expression = expression.replace("++","+")
        expression = expression.replace("-","+-")
        if len(expression)>0 and expression[0] =="+":
            expression = expression[1:]
        nums = expression.split("+")
        f,d = 0,1
        for st in nums:
            ss = st.split("/")
            f1 = int(ss[0])
            d1 = int(ss[1])
            f,d = fracAdd(f,d,f1,d1)
            if f*d<0:
                f = -abs(f)
                d = abs(d)
        return str(f)+"/"+str(d)
a = input()
s = Solution()
print(s.fractionAddition(a))