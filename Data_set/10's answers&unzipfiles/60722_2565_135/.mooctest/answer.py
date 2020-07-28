class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        li = sorted((nums1 + nums2))
        s = len(li)
        if s % 2:
            return float(li[s // 2])
        else:
            return float((li[s // 2 - 1] + li[s // 2]) / 2)

b1 = input().split(',')
c1= []
for i in b1:
    c1.append(int(i))

b2 = input().split(',')
c2= []
for i in b2:
    c2.append(int(i))
s = Solution()
print("%.5f" % s.findMedianSortedArrays(c1,c2))