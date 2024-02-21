# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotate(self,head):
        curr=head
        while curr:
            if curr.next and curr.next.next is None:
                temp=curr.next
                curr.next=None
                temp.next=head
                head=temp
            elif curr.next:
                curr=curr.next
            else:
                return head
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return head
        count=0
        curr=head
        while curr:
            curr=curr.next
            count+=1
        k=k%count
        for i in range(k):
            head=self.rotate(head)
        return head