class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2

        if len(A) > len(B):
            A, B = B, A 
        

        total = len(nums1) + len(nums2)
        half = total // 2 

        low = 0 
        high = len(A) - 1       

        while True: 
            
            i = (low + high) // 2  # pointer for A (everything <= i included in left partition)
            j = half - i - 2

            # calculate starting elements in each partion 
            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[i + 1] if i + 1< len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[j + 1] if j + 1 < len(B) else float('inf')

            # validate partitions
            if Aleft <= Bright and Bleft <= Aright:

                if total % 2 == 0:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2 
                else:
                    return min(Aright, Bright)
            elif Aleft > Bright:
                high = i - 1
            else:
                low = i + 1 
        