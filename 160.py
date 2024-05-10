# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        s=set()
        curr1=headA
        while curr1:
            s.add(curr1)
            if curr1.next:
                curr1=curr1.next
            else:
                break
        curr2=headB
        while curr2:
            if curr2 in s:
                return curr2
            if curr2.next:
                curr2=curr2.next
            else:
                break
        return None 
        
