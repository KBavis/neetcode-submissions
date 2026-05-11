class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0 
        high = len(nums)  -1

        min_val = float('inf')

        while low <= high:

            # check if sorted 
            if nums[low] <= nums[high]:
                return min(nums[low], min_val)
            

            mid = (low + high) // 2
            min_val = min(nums[mid], min_val)

            if nums[low] <= nums[mid]:
                low = mid + 1 
            else:
                high = mid - 1 
        

        return min_val 