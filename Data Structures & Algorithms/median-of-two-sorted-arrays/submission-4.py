class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1 
        
        x, y = len(nums1), len(nums2)

        low = 0
        high = x

        while low <= high:

            # find partitions 
            nums1_partition = (low + high) // 2 
            nums2_partition = (x + y + 1) // 2 - nums1_partition  # Fixed!

            # determine maxes and mins 
            num1_maxLeft = nums1[nums1_partition - 1] if nums1_partition > 0 else float('-inf')
            num1_minRight = nums1[nums1_partition] if nums1_partition < x else float('inf')  # Fixed!

            num2_maxLeft = nums2[nums2_partition - 1] if nums2_partition > 0 else float('-inf')  # Fixed!
            num2_minRight = nums2[nums2_partition] if nums2_partition < y else float('inf')  # Fixed!

            # determine if we found correct partitions 
            if num1_maxLeft <= num2_minRight and num2_maxLeft <= num1_minRight:

                # found median! 
                if (x + y) % 2 == 0:  # Fixed parentheses!
                    return (min(num2_minRight, num1_minRight) + max(num1_maxLeft, num2_maxLeft)) / 2  # Fixed division!
                else:
                    return max(num1_maxLeft, num2_maxLeft)  # Fixed! Max of left, not min of right
            elif num1_maxLeft > num2_minRight:
                high = nums1_partition - 1  # Fixed variable name!
            else:
                low = nums1_partition + 1  # Fixed variable name!
        
        return -1
        