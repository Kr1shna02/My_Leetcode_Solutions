
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict={}
        for x in nums:
            if x in Dict:
                t=Dict[x]
                Dict[x]=(t+1)
            else:
                Dict[x]=1
        temp=[]
        for x in Dict:
            a=[]
            a.append(x)
            a.append(Dict[x])
            temp.append(a)
        for i in range(len(temp)):
            for j in range(len(temp)-i-1):
                if temp[j][1]<temp[j+1][1]:
                    temp[j],temp[j+1]=temp[j+1],temp[j]
        res=[]
        for i in range(k):
            res.append(temp[i][0])
        return res
        
