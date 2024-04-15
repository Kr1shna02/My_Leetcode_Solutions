# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.head=ListNode()
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        val1=[]
        for x in lists:
            curr=x
            while curr:
                val1.append(curr.val)
                if curr.next:
                    curr=curr.next
                else:
                    break
        val1.sort()
        self.head=None
        if len(val1)==0:
            return self.head
        n=ListNode(val1[0])
        self.head=n
        temp=self.head.next
        for i in range(1,len(val1)):
            n=ListNode(val1[i])
            curr=self.head
            while curr:
                if curr.next==None:
                    curr.next=n
                    break
                else:
                    curr=curr.next
        return self.head

        
