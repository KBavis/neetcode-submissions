class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2 

        # enusre A is the smaller of the two lists (optimize binary search on smaller of the two)
        if len(B) < len(A):
            A, B = B, A 
        

        l, r = 0, len(A) - 1 

        while True: # we know there is a median!

            """
                # i --> the index of the LAST element we're taking from array A 
                # j --> the index of the LAST element we're taking from array B 

                1. Given i is the last index in left partition for A, we have i + 1 elements in left partition 
                2. We ONLY want our left partition to have exactly HALF the elements (i.e len(nums1) + len(nums2))
                3. So, to determine j, we use equation ==> (i + 1) + (j + 1) = half 
                4. Solving for j gets us --> half - i - 2 
                5. This ensures (i + 1) + (j + 1) == half
            """
            i = (l + r) // 2 
            j = half - i - 2

            Aleft = A[i] if i >= 0 else float("-inf") 
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float('inf')
            
            """
                1. If the rightMost position in A's left partition is less than leftMost position n B's right partition 
                2. If the rightMost position in B's left partiion is less than leftMosjt position in A's right partion
                3. If this is hte case, we correctly found partitions
            """
            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright) # since we ensure A & B's left partitions are == half, that means right partition has more elements 
                
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = i - 1 # too many elements in A's left partition, need to remove some 
            else:
                l = i + 1 
        

        

