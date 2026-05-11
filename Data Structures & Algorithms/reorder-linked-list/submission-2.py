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
        l1, l2 = head, mid.next 
        mid.next = None 

        l2 = self.reverse(l2)

        while l1 and l2:
            l1_next = l1.next 
            l2_next = l2.next if l2 else None 

            l1.next = l2
            l2.next = l1_next

            l1 = l1_next
            l2 = l2_next 


    
    def reverse(self, head):

        temp = None 
        while head:
            next_node = head.next
            head.next = temp 
            temp = head 
            head = next_node 
                
        return temp
    
    
    def find_mid(self, head):

        slow = head 
        fast = head 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow 
