class Node:
    def __init__(self, val):
        self.val = val 
        self.next = None 
        self.prev = None 

class Solution:
    def maxCoins(self, nums: List[int]) -> int:

        # ensure out of bouns are single digits 
        self.left_most = Node(1)
        self.right_most = Node(1)
        
        self.left_most.next = self.right_most
        self.right_most.prev = self.left_most 
        
        # insert nodes into doubly linked list 
        left = self.left_most
        for num in nums:
            node = Node(num)
            self.insert_node(node, left)
            left = node
        

        # leverage linked list for backtracking 
        return self.backtrack()
    

    def backtrack(self):

        max_coins = 0 
        curr = self.left_most.next 

        if curr == self.right_most:
            return 0 
        

        while curr != self.right_most:

            # calculate coins if we pop this ballon 
            coins = curr.prev.val * curr.val * curr.next.val 

            left_node = curr.prev # store reference to prev
            self.remove_node(curr)

            total = coins + self.backtrack() 
            max_coins = max(max_coins, total)

            self.insert_node(curr, left_node)

            curr = curr.next 
        

        return max_coins 



    

    def insert_node(self, node, left_most):

        next_node = left_most.next 

        next_node.prev = node 
        node.next = next_node 
        node.prev = left_most 

        left_most.next = node 


    

    def remove_node(self, node):
        
        prev = node.prev 
        next_node = node.next

        prev.next = next_node 
        next_node.prev = prev 
