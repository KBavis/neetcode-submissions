class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        seen = set(nums)
        longest = 1

        for num in seen:
            if num - 1 not in seen:
                curr = 1 

                while num + 1 in seen:
                    num = num + 1 
                    curr += 1 
                
                longest = max(longest, curr)
        

        return longest 