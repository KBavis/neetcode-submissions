class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        low = 0 
        high = len(nums) - 1

        min_value = float('inf')

        while low <= high:
            if nums[low] < nums[high]:
                min_value = min(min_value, nums[low])
                break

            mid = (low + high) // 2
            min_value = min(min_value, nums[mid])

            if nums[mid] >= nums[low]:
                low = mid + 1
            else:
                high = mid - 1
        
        return min_value
