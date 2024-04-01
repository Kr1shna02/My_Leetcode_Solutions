class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        for i in range(len(heights)):
            for j in range(0,len(heights)-i-1):
                if heights[j]<heights[j+1]:
                    temp=heights[j]
                    heights[j]=heights[j+1]
                    heights[j+1]=temp
                    temp1=names[j]
                    names[j]=names[j+1]
                    names[j+1]=temp1
        return names