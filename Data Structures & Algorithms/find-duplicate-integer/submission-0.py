class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        """
        Intution: To make this solution O(1), we will need to leverage the concept of a "cycle" being present in this code 
                    Rather than going through and creating individual nodes, we will simply just use the list we have with O(1) lookup
                    We do this by using slow/fast pointers to detect the cycle as usual 

                    Once we have found a cycle, we use Floyds algorithm in order to determine what value appears multiple times 

                    How it works: The distance between the "start" of a cycle and the "original start" of linked list are equal 
        """



        slow, fast = 0, 0 

        while True:

            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break 
        

        slow2 = 0 
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]

            if slow == slow2:
                break 
        

        return slow