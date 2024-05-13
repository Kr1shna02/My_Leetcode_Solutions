class Solution:
    def inttoBinary(self,num):
        res=[]
        if num==0:
            return "0"
        while num!=0:
            if num%2==0:
                res.append("0")
                num=num//2
            else:
                res.append("1")
                num=num//2
        res.reverse()
        return "".join(res)

    def Binarytoint(self,binary):
        binary=binary[::-1]
        num=0
        for i in range(len(binary)):
            num+=(2**i)*int(binary[i])
        return num
    def addBinary(self, a: str, b: str) -> str:
        number=self.Binarytoint(a)+self.Binarytoint(b)
        return self.inttoBinary(number)
