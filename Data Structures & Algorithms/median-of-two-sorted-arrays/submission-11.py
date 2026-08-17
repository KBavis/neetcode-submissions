class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        

        x, y = len(nums1), len(nums2)
        total = x + y 
        half = total // 2 


        low = 0
        high = x 
        while low <= high:

            i = (low + high) // 2 # number of element in left half of num1 
            j = half - i  # number of element in left half of num2

            nums1_left = nums1[i - 1] if i - 1 >= 0 else float('-inf')
            nums1_right = nums1[i] if i < x else float('inf')
            nums2_left = nums2[j - 1] if j - 1 >= 0 else float('-inf')
            nums2_right = nums2[j] if j < y else float('inf')

            if nums1_left <= nums2_right and nums2_left <= nums1_right:

                if total % 2 != 0:
                    return min(nums1_right, nums2_right)
                else:
                    return (max(nums1_left, nums2_left) + min(nums2_right, nums1_right)) / 2
            elif nums1_left > nums2_right:
                high = i - 1 
            else:
                low = i + 1 
        