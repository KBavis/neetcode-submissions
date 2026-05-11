# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not self.hasKNodes(head, k):
            return head 
        

        # reverse K nodes and get back relevant pointers 
        new_head, tail, start_of_new_k_nodes = self.reverse(head, k)
        tail.next = self.reverseKGroup(start_of_new_k_nodes, k)

        return new_head 
    

    def reverse(self, head, k):
        count = 0
        original_head = head

        prev = None 
        while head and count < k:
            next_node = head.next 
            head.next = prev 
            prev = head 
            head = next_node 
            count += 1 
        

        return prev, original_head, head
   

    def hasKNodes(self, head, k):

        count = 0 
        while head and count < k:
            head = head.next 
            count += 1 
        
        return count == k 