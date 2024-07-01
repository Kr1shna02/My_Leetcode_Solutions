class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones)!=1:
            stones.sort()
            print(stones)
            x=stones[-1]
            stones.pop()
            y=0
            if len(stones)>0:
                y=stones[-1]
                stones.pop()
            if x>=y:
                stones.append(x-y)
            print(stones)
        return stones[0]
