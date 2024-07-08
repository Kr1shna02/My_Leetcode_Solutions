class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numbers=[]
        opertions=[]
        symbols={'*','-','/','+'}
        while len(tokens)!=0:
            if tokens[0] not in symbols:
                numbers.append(int(tokens[0]))
                tokens.pop(0)
            elif len(numbers)>=2:
                a=numbers[-2]
                b=numbers[-1]
                numbers.pop()
                numbers.pop()
                if tokens[0]=='-':
                    numbers.append(a-b)
                elif tokens[0]=='*':
                    numbers.append(a*b)
                elif tokens[0]=='/':
                    numbers.append(int(a/b))
                elif tokens[0]=='+':
                    numbers.append(a+b)
                tokens.pop(0)
            else:
                break
        return numbers[-1]
