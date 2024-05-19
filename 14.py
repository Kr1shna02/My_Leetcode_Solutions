class Solution:
    def m(self,strs):
        res=strs[0]
        for i in range(1,len(strs)):
            if len(strs[i])<len(res):
                res=strs[i]
        return res
    def longestCommonPrefix(self, strs: List[str]) -> str:
        a=self.m(strs)
        pre=""
        for i in range(len(a)):
            t=a[i]
            count=0
            for j in range(len(strs)):
                if t==strs[j][i]:
                    count+=1
            if count==len(strs):
                pre+=t
            else:
                break
        return pre
