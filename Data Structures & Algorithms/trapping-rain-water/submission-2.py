class Solution:
    def trap(self, height: List[int]) -> int:
        
        if not height: 
            return 0 
        

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0 


        while l < r:
            # shift left pointer (since its the minimum of the 2, its the bottleneck)
            if leftMax < rightMax:
                l += 1 
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]

            else: # shift right pointer (since its the minimum of the 2, its the bottleneck)
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        

        return res