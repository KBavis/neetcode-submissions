class Solution:
    def trap(self, height: List[int]) -> int:
        """
            Naive Approach:
                From each height[i], expand right pointer j, while height[i] > height[j]:
                Each point, we accumulate total 

            totalAccumulated += min(maxLeft, maxRight) - height[i]

            iterate through and generate two arrays:
                maxL[i] --> maxHeight to left of this point i
                maxR[i] --> maxHeight to the right of this point i 
        
        """

        l, r = 0, len(height) - 1 
        left_max, right_max = height[l], height[r]
        total = 0

        while l < r:
            
            # left height is limiting factor
            if height[l] < height[r]:
                l += 1 
                left_max = max(left_max, height[l])
                total += left_max - height[l]
            else:
                r -=1 
                right_max = max(right_max, height[r])
                total += right_max - height[r]
            

        return total 