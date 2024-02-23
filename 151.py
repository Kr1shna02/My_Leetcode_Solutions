class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.strip()
        List=s.split(" ")
        result=[]
        for x in List:
            if len(x)>=1:
                result.append(x)
        result.reverse()
        s=" ".join(result)
        return s