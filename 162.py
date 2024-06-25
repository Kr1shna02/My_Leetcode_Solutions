class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 0
        if len(nums)==2:
            if nums[1]>nums[0]:
                return 1
            return 0
        n=0
        if len(nums)%2==0:
            n=len(nums)//2
        else:
            n=len(nums)//2+1
        print(n)
        for i in range(1,n):
            j=len(nums)-i-1
            if nums[i]>nums[i-1] and nums[i]>nums[i+1]:
                return i
            if nums[j]>nums[j-1] and nums[j]>nums[j+1]:
                return j
        if nums[-1]>nums[-2]:
            return nums.index(nums[-1])
        return 0
            
