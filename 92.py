# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left==right:
            return head
        curr=head
        for i in range(left-1):
            curr=curr.next
        curr_t=curr
        stack=[]
        right-=left
        while curr and right>=0:
            stack.append(curr.val)
            curr=curr.next
            right-=1
        stack.reverse()
        while curr_t and len(stack)!=0:
            curr_t.val=stack[0]
            stack.pop(0)
            curr_t=curr_t.next
        return head
