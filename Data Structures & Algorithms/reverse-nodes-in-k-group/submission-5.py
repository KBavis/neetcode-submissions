# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        """
            a) BASE CASE:
                - there are < k nodes remaining in linked list 
                - return just the head and don't flip 
            

            Recursively reverse nodes 

            b) reverse the nodes (only the first k nodes)
                    - save reference to "new head", this is what our recursion returns 
                    - save references to "original head", this is now the tail 
                    - save refernce to "next start", this is arg we pass to recursive function 
            c) set the "tail" next to the recurse of the next function call 
                    tail.next = reverseKGroup(next_head) 
            d) function to check if AT LEAST k nodes remain (stop counting when we get to 5)
        """

        if not self.hasKNodes(head, k):
            return head 
        

        tail, new_head, next_k_group_head = self.reverseKNodes(head, k)
        tail.next = self.reverseKGroup(next_k_group_head, k)
        return new_head 


    def reverseKNodes(self, head, k):

        tail = head 
        count = 0
        
        temp = None 
        while head and count < k:
            next_node = head.next 
            head.next = temp 
            temp = head 
            head = next_node 
            count += 1 
        

        return tail, temp, head
    

    def hasKNodes(self, head, k):
        count = 0

        while head and count < k:
            head = head.next 
            count += 1 
        
        return count == k