# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        # find mid point 
        mid = self.find_mid(head)

        l2 = mid.next
        l1 = head

        mid.next = None 

        # reverse mid 
        l2 = self.reverse(l2)

        while l2:
            l1_next = l1.next 
            l2_next = l2.next

            l1.next = l2 
            l2.next = l1_next 

            l1 = l1_next
            l2 = l2_next 


    
    def reverse(self, head):

        prev = None 
        while head:
            next_node = head.next
            head.next = prev 
            prev = head 
            head = next_node
        
        return prev 

    def find_mid(self, head):

        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        return slow 