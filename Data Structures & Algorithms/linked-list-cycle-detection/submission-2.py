# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        l1 = head 
        l2 = head 


        while l2 and l2.next: 
            
            l1 = l1.next 
            l2 = l2.next.next 

            if l1 == l2:
                return True 
            
        
        return False 