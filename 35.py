class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)-1):
            if(nums[i]==target):
                return i
            elif(nums[i]<target<nums[i+1]):
                return i+1
        if target==nums[len(nums)-1]:
            return len(nums)-1
        if target<nums[0]:
            return 0
        return len(nums) 