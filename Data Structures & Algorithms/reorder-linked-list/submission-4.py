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
        mid.next = None 

        l1 = head 


        # reverse l2 
        l2 = self.reverse(l2)

        # intersect lists 

        while l1 and l2:

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
        fast = head.next 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        return slow