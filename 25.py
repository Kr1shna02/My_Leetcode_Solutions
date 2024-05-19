# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self,nums):
        for i in range(len(nums)//2):
            nums[i].val,nums[-1-i].val=nums[-1-i].val,nums[i].val
    def size(self,head):
        s=0
        while head:
            s+=1
            if head.next:
                head=head.next
            else:
                break
        return s
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        s=self.size(head)
        s=s//k
        curr=head
        for i in range(s):
            nums=[]
            for _ in range(k):
                nums.append(curr)
                curr=curr.next
            self.reverse(nums)
        return head
