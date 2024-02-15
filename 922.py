class Solution(object):
    def sortArrayByParityII(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        even=[]
        odd=[]
        for x in nums:
            if x%2==0:
                even.append(x)
            else:
                odd.append(x)
        even.sort()
        odd.sort()
        result=[]
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