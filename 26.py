class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        if len(nums)==2:
            if nums[0]!=nums[1]:
                return 2
            else:
                nums.pop(1)
                return 1
        Set=list(set(nums))
        Set.sort()
        for x in Set:
            count=nums.count(x)
            print(count)
            if count!=1:
                index=nums.index(x)
                for i in range(count-1):
                    nums.pop(index)
        return len(nums)
