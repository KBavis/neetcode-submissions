# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        if not lists:
            return None

        while len(lists) > 1:

            merged_lists = []

            for i in range(0, len(lists), 2):
                l1 = lists[i]
                l2 = lists[i + 1] if i + 1 < len(lists) else None

                merged_lists.append(self.mergeTwo(l1, l2))
            
            lists = merged_lists
        
        return lists[0]



    
    def mergeTwo(self, l1, l2):

        dummy = ListNode(-1)
        curr = dummy

        while l1 or l2:
            l1_val = l1.val if l1 else float('inf')
            l2_val = l2.val if l2 else float('inf')

            if l1_val < l2_val:
                curr.next = ListNode(l1_val)
                l1 = l1.next
            else:
                curr.next = ListNode(l2_val)
                l2 = l2.next 
            
            curr = curr.next
        
        return dummy.next