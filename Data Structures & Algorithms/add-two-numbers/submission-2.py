# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2 or carry > 0:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            curr_sum = l1_val + l2_val + carry 

            carry = curr_sum // 10 
            value = curr_sum % 10 

            l1 = l1.next if l1 else None 
            l2 = l2.next if l2 else None 

            curr.next = ListNode(value)
            curr = curr.next 
        

        return dummy.next 