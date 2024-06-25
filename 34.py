class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res=[-1,-1]
        i=0
        j=0
        if target in nums:
            i=nums.index(target)
            res[0]=i
            nums.reverse()
            j=nums.index(target)
            j=len(nums)-j-1
            res[1]=j
        return res
        
