# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode() 
        head = dummy

        while list1 or list2:

            l1_val = list1.val if list1 else float('inf')
            l2_val = list2.val if list2 else float('inf')

            if l1_val <= l2_val:
                head.next = list1 
                list1 = list1.next 
            else:
                head.next=  list2
                list2 = list2.next 
            
            head = head.next 
        

        return dummy.next 