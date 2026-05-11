# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        

        counter = 0 
        fast = head
        slow = head
        
        while counter < n:
            fast = fast.next 
            counter += 1
        

        if not fast:
            return head.next


        while fast and fast.next:
            slow = slow.next
            fast = fast.next 
        

        slow.next = slow.next.next if slow.next else None 

        return head