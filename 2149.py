class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        pos=[]
        neg=[]
        result=[]
        for i in range(len(nums)):
            if nums[i]>0:
                pos.append(nums[i])
            else:
                neg.append(nums[i])
        j=0
        k=0
        for i in range(len(nums)):
            if i%2==0:
                result.append(pos[j])
                j+=1
            else:
                result.append(neg[k])
                k+=1
        return result