# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev=None
        curr=head
        while curr:
            Next=curr.next
            curr.next=prev
            prev=curr
            if Next is not None:
                curr=Next
            else:
                break
        if prev is None:
            return None 

        result = prev
        high = prev.val
        curr = prev.next 
        while curr:
            if curr.val >= high:
                high = curr.val
                result.next = curr
                result = result.next 
            curr = curr.next

        result.next = None 
        prev1=None
        curr=prev
        while curr:
            Next=curr.next
            curr.next=prev1
            prev1=curr
            if Next:
                curr=Next
            else:
                break
        return prev1