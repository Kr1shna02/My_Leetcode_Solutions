class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                t1=str(nums[i])+str(nums[j])
                t2=str(nums[j])+str(nums[i])
                if t1<t2:
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        res=""
        for x in nums:
            res+=str(x)
        while True:
            if res[0]=="0" and len(res)!=1:
                res=res[1:]
            else:
                break
        return res

    

        
