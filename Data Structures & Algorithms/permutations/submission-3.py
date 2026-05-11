class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        
        def backtrack(idx):
            if idx == len(nums):
                res.append(list(nums))
                return 
            
            for i in range(idx, len(nums)):
                # Swap to put nums[i] at position idx
                nums[idx], nums[i] = nums[i], nums[idx]
                
                # Fix the NEXT position (idx+1, not i+1)
                backtrack(idx + 1)  # ✅ Fixed!
                
                # Undo the swap
                nums[idx], nums[i] = nums[i], nums[idx]
        
        backtrack(0)
        return res