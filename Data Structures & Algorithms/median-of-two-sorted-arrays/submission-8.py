class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    
        return self.naive(nums1, nums2)

    def naive(self, nums1, nums2):

        p1 = 0
        p2 = 0 
        total_len = len(nums1) + len(nums2)
        is_even = total_len % 2 == 0
        target = (total_len // 2) + 1 
        prev_num = None 

        while p1 < len(nums1) or p2 < len(nums2):
            curr_num1 = nums1[p1] if p1 < len(nums1) else float('inf')
            curr_num2 = nums2[p2] if p2 < len(nums2) else float('inf')

            if curr_num1 < curr_num2:
                curr_num = curr_num1 
                p1 += 1 
            else:
                curr_num = curr_num2
                p2 += 1 
            

            if target == p1 + p2:
                return self.get_res(curr_num, prev_num, is_even)
            
            prev_num = curr_num 
        

    def get_res(self, curr, prev, is_even):

        if is_even:
            return (curr + prev) / 2 if prev and curr + prev != 0 else 0
        else:
            return curr


