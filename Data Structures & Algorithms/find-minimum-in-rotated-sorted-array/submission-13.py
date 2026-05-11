class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # if nums[low] <= nums[high]:
            # return the min between nums[low] and what current min is 
        

        # if nums[mid] >= nums[low] --> min on other side 

        low = 0 
        high = len(nums) - 1
        min_val = float('inf')

        while low <= high:
            # stop searching when its sorted 
            if nums[low] <= nums[high]:
                return min(min_val, nums[low])

            mid = (low + high) // 2 
            min_val = min(nums[mid], min_val)
            
            if nums[mid] >= nums[low]:
                low = mid + 1 
            else:
                high = mid - 1 
        

        return min_val 

