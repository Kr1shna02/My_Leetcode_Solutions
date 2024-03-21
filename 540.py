class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            if nums[1]>nums[0]:
                return nums[1]
            return nums[0]
        for j in range(1,len(nums)-1):
            if nums[j]!=nums[j-1] and nums[j]!=nums[j+1]:
                return nums[j]
        if nums[0]!=nums[1]:
            return nums[0]
        if nums[len(nums)-1]!=nums[len(nums)-2]:
            return nums[len(nums)-1]
        return 0