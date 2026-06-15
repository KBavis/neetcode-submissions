class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
            When processing recursive function in this order, we should go through and account for 
            duplicates by 

            a) sorting the nums --> O(nlogn)
            b) in the case that we're on a different level of recursion, we shouldn't recurse down that branch

            we either take the number or we don't
        """


        nums.sort() 
        self.res = []

        def subset(idx: int, so_far: list): 

            self.res.append(list(so_far))

            for i in range(idx, len(nums)):
                
                # validate that don't duplicate sister branches by skipping duplicates on same level of recursion 
                if i > idx and nums[i] == nums[i - 1]:
                    continue 
                    
                so_far.append(nums[i])
                subset(i + 1, so_far)
                so_far.pop() 
        

        subset(0, [])
        return self.res