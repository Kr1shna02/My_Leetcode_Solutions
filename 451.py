class Solution:
    def frequencySort(self, s: str) -> str:
        pairs,elements={},[]
        for i in range(len(s)):
            if s[i] in pairs.keys():
                pairs[s[i]]+=1
            else:
                pairs[s[i]]=1
        for x,y in pairs.items():
            temp=[y,x]
            elements.append(temp)
        for i in range(len(elements)):
            for j in range(0,len(elements)-i-1):
                if elements[j][0]<elements[j+1][0]:
                    elements[j],elements[j+1]=elements[j+1],elements[j]
        res=""
        for x in elements:
            for j in range(x[0]):
                res+=x[1]
        return res
        
