class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """
            O(log(m + n)) time --> indicates some sort of "binary search" aspect to it all 

            This means simply navigating through each array (O(n + m)) is not going to be sufficient in making this determination 

            Tricky Part:
                Cannot simply perform binary search given the fact that greatest element in n1 is not necessaryily 
                bigger than greatest element in nums2 

            Goal:
                Partition the arrays in a way where 
                    a) the rightMost element in leftPartition is <= leftMost element in each rightPartition
                    b) the leftMost element in rightPartition is >= rightMost element in each left partition

        """


        # always perform binary search on the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 


        x, y = len(nums1), len(nums2)
        total = x + y 
        half = total // 2 


        low = 0 
        high = x # NOTE: high is usually x - 1 when searching for valid index, but in this case, were looking for partition 
        while low <= high:
            
            i = (low + high) // 2 # number of elements in the nums1 left half
            j = half - i # number of elements in the nums2 left half

            nums1_left = nums1[i - 1] if i - 1 >= 0 else float('-inf') # NOTE: i in this case is a count, not a postion marker
            nums1_right = nums1[i] if i < x else float('inf')
            nums2_left = nums2[j - 1] if j - 1 >= 0 else float('-inf')
            nums2_right = nums2[j] if j < y else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:
                # correct partition found 

                if total % 2 != 0:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums1_right, nums2_right)) / 2
            elif nums1_left > nums2_right:
                # took too many elements in left partition 
                high = i - 1 
            else:
                low = i + 1 
            