# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:        
        head=None
        if not list1 and not list2:
            return list1
        elif not list1 and list2:
            head=list2
        elif list1 and not list2:
            head=list1
        else:
            head=list1
            curr=head
            while curr:
                if curr.next:
                    curr=curr.next
                else:
                    break
            curr.next=list2
        
        curr=head
        while curr:
            curr1=head
            while curr1:
                if curr1.val>=curr.val:
                    curr1.val,curr.val=curr.val,curr1.val
                if curr1.next:
                    curr1=curr1.next
                else:
                    break
            if curr.next:
                curr=curr.next
            else:
                break
        return head
