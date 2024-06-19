class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        res=set()
        for x in nums:
            if x not in res:
                res.add(x)
            else:
                res.remove(x)
        return list(res)
