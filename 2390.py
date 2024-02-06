class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        result=[]
        for x in s:
            if(x=='*'):
                result.pop()
            else:
                result.append(x)
        return "".join(result)