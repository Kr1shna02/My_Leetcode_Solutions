# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        Set=set()
        curr=head
        while curr:
            Set.add(curr)
            if curr.next is not None:
                curr=curr.next
                if curr in Set:
                    return 1
            elif curr.next is None:
                return 0
        return 0