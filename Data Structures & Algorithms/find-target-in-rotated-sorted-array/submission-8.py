class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        low = 0 
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2 
            if nums[mid] == target:
                return mid 
            
            # check if LHS is sorted 
            if nums[low] <= nums[mid]:
                
                # if its within the sorted LHS 
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1 
                else:
                    low = mid + 1
            else:

                # if RHS sorted and target in range 
                if nums[mid] < target and nums[high] >= target:
                    low = mid + 1 
                else:
                    high = mid - 1 


        return -1        


