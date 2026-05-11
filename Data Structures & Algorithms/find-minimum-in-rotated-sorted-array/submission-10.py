class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return 

        low = 0 
        high = len(nums) - 1

        min_val = float('inf')

        while low <= high:

            if nums[low] <= nums[high]:
                min_val = min(min_val, nums[low])
                break 
            
            mid = (low + high) // 2 
            min_val = min(min_val, nums[mid])

            if nums[low] <= nums[mid]:
                low = mid + 1 
            else:
                high = mid - 1 
        

        return min_val