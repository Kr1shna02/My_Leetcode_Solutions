class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        tar=ord(target)
        print(type(tar))
        result=[]
        for i in range(len(letters)):
            temp=ord(letters[i])-tar
            if temp>0:
                result.append(temp)
        result.sort()
        print(result)
        if len(result)!=0 and result[0]+tar>tar:
            return chr(result[0]+tar)
        return letters[0]