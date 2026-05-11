# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not self.hasKNodes(head, k):
            return head 
        

        # reverse k nodes 
        new_tail, next_group_head, new_head = self.reverseK(head, k)

        new_tail.next = self.reverseKGroup(next_group_head, k)

        return new_head 
    

    def reverseK(self, head, k):

        count = 0 
        tail = head 

        prev = None
        while count < k and head:
            next_node = head.next 
            head.next = prev 
            prev = head 
            head = next_node 

            count +=1 

        return tail, next_node, prev 
            
    

    def hasKNodes(self, head, k):
        count = 0

        while head and count < k:
            count += 1 
            head = head.next 

        return count == k