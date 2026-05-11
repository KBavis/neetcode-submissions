# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        mid = self.find_mid(head)

        next_head = mid.next 
        mid.next = None 

        reversed_head = self.reverse(next_head)

        print(reversed_head)
        print(head)

        l1 = head
        l2 = reversed_head 

        while l2:
            l1_next = l1.next 
            l2_next = l2.next

            l1.next = l2 
            l2.next = l1_next 

            l1 = l1_next
            l2 = l2_next 



    def reverse(self, head):

        temp = None 
        while head:
            next_node = head.next 
            head.next = temp 
            temp = head 
            head = next_node 
        

        return temp

    def find_mid(self, head):

        slow = head 
        fast = head 

        while fast and fast.next and fast.next.next:
            slow = slow.next 
            fast = fast.next.next 
        

        return slow