class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        elements = set(nums)
        max_length = 0

        for i in range(len(nums)):
            curr = nums[i]
            
            # if at smallest element in a potential sequence 
            if curr - 1 not in elements:
                curr_length = 1

                while curr + 1 in elements:
                    curr_length += 1
                    curr += 1
                
                max_length = max(max_length, curr_length)
        

        return max_length
        