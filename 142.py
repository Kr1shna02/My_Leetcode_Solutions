# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        Set=set()
        curr=head
        n=ListNode(None)
        while curr:
            Set.add(curr)
            if curr.next is not None:
                curr=curr.next
                if curr in Set:
                    return curr
            elif curr.next is None:
                return None
        return None