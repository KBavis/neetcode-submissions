class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        values = set(nums)

        max_consec = 1 

        for num in values:

            # skip counting if not lowest value in sequence
            if num - 1 in values:
                continue

            curr = 1 
            while num + 1 in values:
                 num += 1
                 curr += 1 
            
            max_consec = max(max_consec, curr)
        

        return max_consec 