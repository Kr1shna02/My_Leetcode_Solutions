# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l1=[]
        l2=[]
        curr=head
        while curr:
            if curr.val<x:
                l1.append(curr.val)
            else:
                l2.append(curr.val)
            if curr.next:
                curr=curr.next
            else:
                break
        l1.extend(l2)
        curr=head
        while curr:
            curr.val=l1[0]
            l1.pop(0)
            if curr.next:
                curr=curr.next
            else:
                break
        return head
