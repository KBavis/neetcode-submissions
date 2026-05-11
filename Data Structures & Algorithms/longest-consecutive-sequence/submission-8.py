class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        seen = set() 
        for num in nums:
            seen.add(num)
        
        longest = 0

        for num in nums:
            if num - 1 not in seen:
                count = 1 
                curr = num 

                while curr + 1 in seen:
                    curr = curr + 1 
                    count += 1 
            
                longest = max(count, longest)


        return longest 