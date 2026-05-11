class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        """
            three seperate indicies (i, j, k) that point to values summing to 0 

            these values must NOT equal each other 

            ensure that they are distinct 

            -1,0,1,2,-1,-4

            -4, -1, -1, 0, 1, 2
        """

        nums.sort()  # O(nlogn)

        i = 0 
        res = [] 

        while i < len(nums):

            j = i + 1 
            k = len(nums) - 1

            while j < k: 

                curr_sum = nums[i] + nums[j] + nums[k]

                if curr_sum == 0:
                    res.append([nums[i], nums[j], nums[k]])

                    # skip duplicate j's 
                    j += 1 
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1 
                    

                    # skip duplicate k's 
                    k -= 1
                    while k > j and nums[k] == nums[k + 1]:
                        k -= 1 
                elif curr_sum > 0:
                    k -= 1 
                else:
                    j += 1 
            
            i += 1
            while i < len(nums) and nums[i] == nums[i - 1]:
                i += 1 
        

        return res 


