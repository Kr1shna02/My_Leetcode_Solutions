class Solution:
    def sortSentence(self, s: str) -> str:
        List=s.split(" ")
        for i in range(len(List)):
            for j in range(0,len(List)-i-1):
                if int(List[j][-1])>int(List[j+1][-1]):
                    temp=List[j]
                    List[j]=List[j+1]
                    List[j+1]=temp
        print(List)
        result=""
        for x in List:
            l=len(x)
            result+=x[0:l-1]
            result+=" "
        return result.rstrip()