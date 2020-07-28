class Solution(object):
    def distributeCandies(self, candies, num_people):

        ans = [0] * num_people
        candy = 1
        while candies >= 0:
            for i in range(num_people):
                if candy < candies:
                    ans[i] += candy
                    candies -= candy
                    candy += 1
                else:
                    ans[i] += candies
                    return ans
a = int(input())
b = int(input())
s = Solution()
print(s.distributeCandies(a,b))