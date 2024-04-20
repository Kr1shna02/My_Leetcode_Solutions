class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        r1=""
        r2=""
        for i in range(len(s)):
            if s[i]!="#":
                r1+=s[i]
            elif s[i]=="#" and len(r1)!=0:
                r1=r1[0:len(r1)-1]
        for i in range(len(t)):
            if t[i]!="#":
                r2+=t[i]
            elif t[i]=="#" and len(r2)!=0:
                r2=r2[0:len(r2)-1]
        return r1==r2
