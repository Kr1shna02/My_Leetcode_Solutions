class Solution:
    def power(self,a):
        count=0
        while a!=1:
            if a%2==0:
                a=a/2
            else:
                a=3*a+1
            count+=1
        return count

    def getKth(self, lo: int, hi: int, k: int) -> int:
        val=[]
        po=[]
        for i in range(lo,hi+1):
            val.append(i)
            po.append(self.power(i))
        res=[]
        
        for i in range(len(val)):
            j=po.index(min(po))
            po[j]=1001
            res.append(val[j])
        return res[k-1]
