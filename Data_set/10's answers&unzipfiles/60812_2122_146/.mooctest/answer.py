class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """
        if z == 0:
            return True
        if x+y < z:
            return False
        if x>y:
            x,y=y,x
        if x == 0:
            return y==z
        while y%x != 0:
            y,x = x,y%x
        return z%x==0
x = int(input())
y = int(input())
z = int(input())
s = Solution()
print(s.canMeasureWater(x,y,z))