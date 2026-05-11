# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head or not head.next:
            return 

        # find mid 
        mid = self.find_mid(head)

        l2 = mid.next 
        mid.next = None 

        # reverse l2 
        l2 = self.reverse(l2)
        l1 = head 


        while l1 and l2:
            n1 = l1.next 
            n2 = l2.next 

            l1.next = l2 
            l2.next = n1 

            l1 = n1 
            l2 = n2 
        
    

    def reverse(self, head):

        prev = None 
        while head:
            next_node = head.next
            head.next = prev 
            prev = head 
            head = next_node 
    
        return prev 

    def find_mid(self, head):

        l1 = head 
        l2 = head.next

        while l2 and l2.next:
            l1 = l1.next 
            l2 = l2.next.next
        
        return l1 