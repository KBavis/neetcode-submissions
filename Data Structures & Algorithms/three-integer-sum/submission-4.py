class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        res = []

        i = 0 
        while i < len(nums):

            j = i + 1 
            k = len(nums) - 1


            while j < k:

                curr = nums[i] + nums[j] + nums[k]

                if curr == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    # skip duplicates 
                    j += 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    
                    k -= 1 
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1 
                    
                elif curr > 0:
                    k -= 1 
                else:
                    j += 1 
            
            i += 1 
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1 
        
        return res
