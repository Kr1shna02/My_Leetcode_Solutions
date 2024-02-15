class Solution(object):
    def sortEvenOdd(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result=[]
        odd=[]
        even=[]
        for i in range(len(nums)):
            if i%2==0:
                even.append(nums[i])
            else:
                odd.append(nums[i])
        odd.sort()
        odd.reverse()
        even.sort()
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                result.append(even[j])
                j+=1
            else:
                result.append(odd[k])
                k+=1
        return result