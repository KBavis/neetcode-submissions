class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """ 
        Trivial to solve this problem in O(n) space and O(n) time, but the goal is to make this so that it's a 
        O(1) space, and O(n) time

        I know its something to do with a linked list, and potentially a slow and fast pointer, but don't remember exact 
        algorithm

        """

        slow = fast = nums[0]

        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        

        slow = nums[0]

        while slow != fast: 
            slow = nums[slow]
            fast = nums[fast]
        

        return fast
