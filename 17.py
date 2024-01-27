class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result=[]
        Dict={
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        if len(digits)==0:
            return result
        elif len(digits)==1:
            for i in Dict[digits]:
                result.append(i)
        elif len(digits)==2:
            temp1=Dict[digits[0]]
            temp2=Dict[digits[1]]
            for i in temp1:
                x=""
                for j in temp2:
                    x=i+j
                    result.append(x)
        elif len(digits)==3:
            temp1=Dict[digits[0]]
            temp2=Dict[digits[1]]
            temp3=Dict[digits[2]]
            for i in temp1:
                x=""
                for j in temp2:
                    for k in temp3:
                        x=i+j+k
                        result.append(x)
        elif len(digits)==4:
            temp1=Dict[digits[0]]
            temp2=Dict[digits[1]]
            temp3=Dict[digits[2]]
            temp4=Dict[digits[3]]
            for i in temp1:
                x=""
                for j in temp2:
                    for k in temp3:
                        for l in temp4:
                            x=i+j+k+l
                            result.append(x)
        return result
        