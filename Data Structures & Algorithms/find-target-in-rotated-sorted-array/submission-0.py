class Solution:
    def search(self, nums: List[int], target: int) -> int:
        

        low = 0
        high = len(nums) - 1

        while low <= high:

            mid = (low + high) // 2

            if nums[mid] == target:
                return mid
            # left half is sorted
            elif nums[low] <= nums[mid]:
                # target in lower half 
                if target >= nums[low] and target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                # target in upper half
                if target <= nums[high] and target >= nums[mid]:
                    low = mid + 1
                else:
                    high = mid - 1
        

        return -1
