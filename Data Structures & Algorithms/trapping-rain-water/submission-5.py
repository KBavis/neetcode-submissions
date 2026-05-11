class Solution:
    def trap(self, height: List[int]) -> int:
        

        maxLeft, maxRight = height[0], height[len(height) - 1]
        l, r = 0, len(height) - 1
        
        res = 0
        while l < r:

            # determine which pointer to move based on limiting factor 
            if maxLeft <= maxRight:
                # move left pointer 
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                # move right pointer
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]
        

        return res 