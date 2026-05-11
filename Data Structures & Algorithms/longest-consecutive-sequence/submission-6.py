class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set(nums)
        longest = 0 

        for num in seen:
            if num - 1 not in seen:
                curr = 1
                while num + 1 in seen:
                    num += 1 
                    curr += 1 
                
                longest = max(curr, longest)
        
        return longest 
