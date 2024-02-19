# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        mindistance=[]
        result=[-1,-1]
        curr=head
        num1=curr.val
        curr=curr.next
        count=2
        while curr:
            if curr.next is not None:
                num2=curr.next.val
                if curr.val>num1 and curr.val>num2:
                    mindistance.append(count)
                elif curr.val<num1 and curr.val<num2:
                    mindistance.append(count)
                count+=1
                num1=curr.val
                curr=curr.next
            else:
                break
        print(mindistance)
        if len(mindistance)>=2:
            Max=mindistance[len(mindistance)-1]-mindistance[0]
            Min=[]
            for i in range(1,len(mindistance)):
                Min.append(mindistance[i]-mindistance[i-1])
            Min.sort()
            result[0]=Min[0]
            result[1]=Max
        return result