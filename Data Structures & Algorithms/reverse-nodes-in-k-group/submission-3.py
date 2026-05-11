# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
            1) check if there is K nodes 
            2) if not k nodes, return head 
            3) if k nodes, store current head 
            4) reverse k nodes of curent list 
            5) set og head .next to revrsed of next 
            5) return reversed head 
        """

        if not self.hasKNodes(head, k):
            return head
        

        new_head, tail, start_of_new_k_nodes = self.reverse(head, k)
        tail.next = self.reverseKGroup(start_of_new_k_nodes, k)

        return new_head

    def reverse(self, head, k):

        prev = None 
        count = 1 

        og_head = head

        while head and count <= k:
            next_node = head.next 
            head.next = prev 
            prev = head 
            head = next_node 
            count += 1 
        
        return prev, og_head, head

    
    def hasKNodes(self, head, k):

        count = 0
        while head and count < k:
            head = head.next
            count += 1 
        

        return count == k