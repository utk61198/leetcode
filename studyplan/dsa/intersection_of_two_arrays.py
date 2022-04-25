#https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        a=[]
        for item in nums1:
            if item in d.keys():
                d[item]=d[item]+1
            else:
                d[item]=1
        for item in nums2:
            if item in d.keys() and d[item]>0:
                d[item]=d[item]-1
                a.append(item)
        return a