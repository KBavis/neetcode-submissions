# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if not head:
            return None 

        fast = head
        slow = head
        
        # stagger 
        for i in range(n):
            if not fast:
                return None 

            fast = fast.next
        
        if not fast:
            return head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        

        slow.next = slow.next.next if slow.next else None 
        return head 
