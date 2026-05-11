class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums)
        longest = 1

        for num in nums:

            if num - 1 not in seen: # smallest # in sequence 
                curr = 1
                while num + 1 in seen: 
                    num += 1
                    curr += 1
                
                longest = max(curr, longest)
        
        return longest 


