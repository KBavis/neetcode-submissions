class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() # nlogn --> 
        i = 0 
        result = [] 
        while i < len(nums):
            j = i + 1 
            k = len(nums) - 1

            while j < k: 
                currSum = nums[i] + nums[j] + nums[k]

                if currSum == 0:
                    result.append([nums[i], nums[j], nums[k]]) 

                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    

                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1 

                elif currSum > 0:
                    k -= 1
                else:
                    j += 1 
            

            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1 
        

        return result 