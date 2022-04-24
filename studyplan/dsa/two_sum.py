class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=0
        y=0
        s=set()
        for i in nums:
            if target-i in s:
                x=target-i
                y=i
            else:
                s.add(i)
        i1=0
        i2=0
        for i in range(len(nums)):
            if nums[i]==x:
                i1=i
        for i in range(len(nums)):
            if nums[i]==y and i!=i1:
                i2=i
                       
        return [i1,i2]
        