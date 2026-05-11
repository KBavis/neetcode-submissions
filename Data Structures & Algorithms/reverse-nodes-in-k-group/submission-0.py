# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        if not self.hasKNodes(head, k):
            return head
        
        # reverse first k nodes
        new_head, new_tail, next_group_start = self.reverse(head, k)

        # recurse on the remainder
        new_tail.next = self.reverseKGroup(next_group_start, k)

        return new_head
    

    def hasKNodes(self, head, k):
        count = 0
        while head and count < k:
            head = head.next
            count += 1
        return count == k


    def reverse(self, head, k):
        count = 0
        prev = None
        curr = head

        while curr and count < k:
            next_node = curr.next      # FIXED
            curr.next = prev
            prev = curr
            curr = next_node
            count += 1

        # prev = new head of reversed group
        # head = original head => now the tail
        # curr = node after the reversed group
        return prev, head, curr
