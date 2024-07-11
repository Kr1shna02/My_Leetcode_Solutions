# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack1,stack2,res,curr1,curr2,carry,head=[],[],[],l1,l2,0,[]
        while curr1:
            stack1.append(curr1.val)
            curr1=curr1.next
        while curr2:
            stack2.append(curr2.val)
            curr2=curr2.next
        while len(stack1)!=0 and len(stack2)!=0:
            s=stack1[0]+stack2[0]+carry
            stack1.pop(0)
            stack2.pop(0)
            if s<=9:
                res.append(s)
                carry=0
            else:
                res.append(s%10)
                carry=s//10
        while len(stack1)!=0:
            s=stack1[0]+carry
            stack1.pop(0)
            if s<=9:
                res.append(s)
                carry=0
            else:
                res.append(s%10)
                carry=s//10
        while len(stack2)!=0:
            s=stack2[0]+carry
            stack2.pop(0)
            if s<=9:
                res.append(s)
                carry=0
            else:
                res.append(s%10)
                carry=s//10
        if carry>0:
            res.append(carry)
        for x in res:
            head.append(ListNode(x))
        for i in range(0,len(head)-1):
            head[i].next=head[i+1]
        return head[0]

    
